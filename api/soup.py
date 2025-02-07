from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
ua = UserAgent()

def get_movie_title():
    item = {'part': 'title', 'tag': 'h1', 'content': 'Heart Eyes', 'attributes': [{'attribute': 'class', 'value': 'unset'}, {'attribute': 'id', 'value': 'media-hero-label'}]}
    url = 'https://www.rottentomatoes.com/m/heart_eyes'
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(item['tag'], {attr['attribute']: attr['value'] for attr in item['attributes']})
    for element in elements:
        if element.get_text().strip() == item['content']:
            result = element.get_text().strip()
    return 'title', result.strip()

def get_tomatometer():
    item = {'part': 'rating', 'tag': 'span', 'content': '85%', 'attributes': [{'attribute': 'class', 'value': 'mop-ratings-wrap__percentage'}]}
    url = 'https://www.rottentomatoes.com/m/heart_eyes'
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(item['tag'], {attr['attribute']: attr['value'] for attr in item['attributes']})
    for element in elements:
        if element.get_text().strip() == item['content']:
            result = float(element.get_text().strip().replace('%', ''))
    return 'rating', result

def get_in_theaters():
    item = {'part': 'inTheaters', 'tag': 'span', 'content': 'Now Playing', 'attributes': [{'attribute': 'class', 'value': 'release-date'}]}
    url = 'https://www.rottentomatoes.com/m/heart_eyes'
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(item['tag'], {attr['attribute']: attr['value'] for attr in item['attributes']})
    for element in elements:
        if element.get_text().strip() == item['content']:
            result = element.get_text().strip() == 'Now Playing'
    return 'inTheaters', result