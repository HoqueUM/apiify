from baml_client.type_builder import TypeBuilder
from baml_client import b
from bs4 import BeautifulSoup
import requests
import asyncio

def main():
    categories = ['critic_score', 'movie_title']
    tb = TypeBuilder()
    for category in categories:
        tb.PageData.add_property(category, tb.string())
    url = 'https://www.rottentomatoes.com/m/alien_romulus'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    res = b.ExtractPageData(soup.prettify(), {"tb": tb})
    print(res)

if __name__ == '__main__':
    main()
