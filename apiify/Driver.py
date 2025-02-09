import pathlib
import json
import subprocess
from mistralai import Mistral, UserMessage
import dotenv
import os

class Driver():
    def __init__(self, data, url, before):
        self.data = data
        self.url = url
        self.before = before
    def build_soup(self):
        print("Building soup...")
        user_agent = "{'User-Agent': ua.random}"
        attributes = "attr['attribute']: attr['value'] for attr in item['attributes']"
        imports = """
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
ua = UserAgent()

"""
        result = imports
        functions = """"""
        for item in self.data:
            function = f"""
def get_{item['part'].lower().replace(' ', '_')}():
    item = {item}
    url = '{self.url}'
    headers = {user_agent}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(item['tag'], {{attr['attribute']: attr['value'] for attr in item['attributes']}})
    for element in elements:
        if element.get_text().strip() == item['content']:
            result = element.get_text().strip()
    return '{item['part']}', result.strip()

"""
            result += function
        self.new_path = pathlib.Path(__file__).parent.parent / 'api'
        self.new_path.mkdir(parents=True, exist_ok=True)
        new_path_temp = self.new_path / 'soup.py'
        final_result = self.adjust_code(result, self.before)
        new_path_temp.write_text(final_result)
        
    def build_flask(self):
        print("Building flask...")
        imports = """
from flask import Flask, request, jsonify
from soup import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    result = {}
"""
        result = imports
        for item in self.data:
            function = f"""
    key, value = get_{item['part'].lower().replace(' ', '_')}()
    result[key] = value
""" 
            result += function
        result += """

    return jsonify(result)
"""
        path = self.new_path / 'app.py'
        path.write_text(result)
        return result
    def adjust_code(self, code, before):
        with open(pathlib.Path(__file__).parent.parent / 'schema.json', 'r') as f:
            schema = json.load(f)
        print(schema)
        dotenv.load_dotenv()
        api_key = os.getenv('MISTRAL_API_KEY')
        client = Mistral(api_key=api_key)
        messages = messages = [
    {
        "role": "system",
        "content": """You are a code adapter that modifies ONLY the item parameters and return values to match schemas. 
        Keep all existing BeautifulSoup logic and code structure intact. Preserve these elements:
        - Function definitions
        - Request handling
        - UserAgent usage
        - Existing parsing logic
        Only modify the item dictionaries and return value formatting."""
    },
    {
        "role": "user",
        "content": f"""Adjust JUST the item parameters and return values in this code:
{code}

Current JSON output structure (keep this format):
{json.dumps(before, indent=2)}

Target schema requirements (modify item dicts to match these):
{json.dumps(schema, indent=2)}

Return the full code with minimal changes - ONLY modify:
1. item dictionary values (part/tag/content/attributes)
2. Return tuple formatting to match schema
Keep all other code EXACTLY as-is including function names and structure.

Output the final code as plain text. Do not wrap it with ```python``` or any other formatting.
"""
    }
]
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    def run(self):
        code = self.build_soup()
        #  self.adjust_code(code, self.before)
        self.build_flask()
        print("Running flask...")
        subprocess.run(['flask', '--app', 'app', '--debug', 'run', '--host', '0.0.0.0', '--port', '5000'], cwd=self.new_path)
