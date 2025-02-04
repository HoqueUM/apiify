import pathlib
import subprocess

class Driver():
    def __init__(self, data, url):
        self.data = data
        self.url = url
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
        new_path_temp.write_text(result)
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
    def run(self):
        self.build_soup()
        self.build_flask()
        print("Running flask...")
        subprocess.run(['flask', '--app', 'app', '--debug', 'run', '--host', '0.0.0.0', '--port', '5000'], cwd=self.new_path)
