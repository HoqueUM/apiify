from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def get_headlines():
    url = 'https://biztoc.com/'
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    ul_elements = soup.find_all('li')
    limiter = 0
    titles = ''
    for ul in ul_elements:
        limiter += 1
        if limiter >= 14:
            titles += ul.text.strip()
            print(ul.text.strip())

    return titles


get_headlines()