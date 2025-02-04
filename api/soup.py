
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
ua = UserAgent()


def get_movie_title():
    item = {'part': 'Movie Title', 'tag': 'sr-text', 'content': 'Heart Eyes', 'attributes': []}
    url = 'https://www.rottentomatoes.com/m/heart_eyes'
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(item['tag'], {attr['attribute']: attr['value'] for attr in item['attributes']})
    for element in elements:
        if element.get_text().strip() == item['content']:
            result = element.get_text().strip()
            return 'Movie Title', result.strip()


def get_tomatometer():
    item = {'part': 'Tomatometer', 'tag': 'rt-text', 'content': '92%', 'attributes': [{'attribute': 'size', 'value': '1.375'}]}
    url = 'https://www.rottentomatoes.com/m/heart_eyes'
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(item['tag'], {attr['attribute']: attr['value'] for attr in item['attributes']})
    for element in elements:
        if element.get_text().strip() == item['content']:
            result = element.get_text().strip()
            return 'Tomatometer', result.strip()

