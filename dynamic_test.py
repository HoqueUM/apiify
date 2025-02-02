from baml_client.type_builder import TypeBuilder
from baml_client import b, reset_baml_env_vars
from bs4 import BeautifulSoup
import requests
import asyncio
import dotenv
import os

dotenv.load_dotenv()
reset_baml_env_vars(dict(os.environ))

def main():
    print("Started...")
    categories = ['tomatometer_html', 'movie_title_html']
    names = ['Tomatometer', 'Movie Title']
    tb = TypeBuilder()
    print("TypeBuilder created...")
    for category in categories:
        tb.PageData.add_property(category, tb.string())
    url = 'https://www.rottentomatoes.com/m/alien_romulus'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Soup created, extracting page data...")
    res = b.ExtractPageData(names, soup.prettify(), {"tb": tb})
    print("Done extracting page data...")    
    print(res)

if __name__ == '__main__':
    main()
