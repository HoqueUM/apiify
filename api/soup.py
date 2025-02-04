
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
