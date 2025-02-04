import pathlib

class Driver():
    def __init__(self):
        pass
    def build_soup(self):
        print("Building soup...")
        result = """
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
def get_data(data):
    ua = UserAgent().random
    response = requests.get(url, headers={'User-Agent': ua})
    soup = BeautifulSoup(response.content, 'html.parser')
    results = {}
    for item in data:
        elements = soup.find_all(item['tag'], {attr['attribute']: attr['value'] for attr in item['attributes']})
        for element in elements:
            if element.get_text().strip() == item['content']:
                results[item['part']] = element.get_text().strip()
                
    return results
"""
        self.new_path = pathlib.Path(__file__).parent.parent / 'api'
        self.new_path.mkdir(parents=True, exist_ok=True)
        new_path_temp = self.new_path / 'soup.py'
        new_path_temp.write_text(result)
    def build_flask(self):
        print("Building flask...")
        result = """
from flask import Flask, request, jsonify
from soup import get_data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify(ge))
"""