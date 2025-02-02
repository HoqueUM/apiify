from baml_client.type_builder import TypeBuilder
from baml_client import b, reset_baml_env_vars
from bs4 import BeautifulSoup
from baml_py.errors import BamlError
from fake_useragent import UserAgent
import requests
import dotenv
import os
from lxml.html.clean import clean_html

dotenv.load_dotenv()
reset_baml_env_vars(dict(os.environ))

def extract_content(categories, names, url):
    assert len(categories) == len(names)
    print("Started...")
    tb = TypeBuilder()
    print("TypeBuilder created...")
    for category in categories:
        tb.PageData.add_property(category, tb.string()).description(f"HTML of {category}")
    
    ua = UserAgent().random
    response = requests.get(url, headers={'User-Agent': ua})
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Soup created, extracting page data...")
    html = soup.prettify()
    html = clean_html(html)

    try:
        res = b.ExtractPageData(names, html, {"tb": tb})
        print("Done extracting page data...")
        result = {}    
        for category in categories:
            method_result = getattr(res, category)
            method_result = method_result.strip() 
            result[category] = method_result
        return result          
    except BamlError as e:
        print(e)

def filter_output(names, output):
    print("TypeBuilder created...")
    res = b.FilterPageData(names, output)
    return res
    

names = ['Movie Title', 'Tomatometer']
metadata = ['part', 'tag', 'content', 'attributes']
categories = [article.lower().replace(' ', '_') + '_html' for article in names]
url = 'https://www.rottentomatoes.com/m/alien_romulus'
res = extract_content(categories, names, url)
output = ''
for item in list(res.values()):
    output += item
res = filter_output(names, output)
print(res)