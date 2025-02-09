from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
ua = UserAgent()

def get_website_title():
    item = {'part': 'title', 'tag': 'h1', 'content': 'Example Domain', 'attributes': []}
    url = 'https://example.com/'
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(item['tag'], {attr['attribute']: attr['value'] for attr in item['attributes']})
    for element in elements:
        if element.get_text().strip() == item['content']:
            result = element.get_text().strip()
    return 'title', result.strip()

def get_content():
    item = {'part': 'rating', 'tag': 'p', 'content': 'This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.', 'attributes': []}
    url = 'https://example.com/'
    headers = {'User-Agent': ua.random}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(item['tag'], {attr['attribute']: attr['value'] for attr in item['attributes']})
    for element in elements:
        if element.get_text().strip() == item['content']:
            result = element.get_text().strip()
    return 'rating', len(result.strip().split())