from baml_client.type_builder import TypeBuilder
from baml_client import b, reset_baml_env_vars
from bs4 import BeautifulSoup
from baml_py.errors import BamlError
from fake_useragent import UserAgent
import requests
import dotenv
import os
from lxml.html.clean import clean_html, Cleaner
def clean_html(html):
    cleaner = Cleaner(
        remove_unknown_tags=False
    )
    return cleaner.clean_html(html)
class GetContent:
    """
    Get the specified content from the given URL.
    """
    def __init__(self, names, url, new_type=False):
        dotenv.load_dotenv()
        reset_baml_env_vars(dict(os.environ))
        self.categories = [name.lower().replace(' ', '_') + '_html' for name in list(names.keys())]
        self.names = names
        self.url = url
        self.new_type = new_type

    def extract_content(self):
        print("Started...")
        tb = TypeBuilder()
        print("TypeBuilder created...")
        for key, val in self.names.items():
            key = key.lower().replace(' ', '_') + '_html'
            print(key)
            print(val)
            tb.PageData.add_property(key, tb.string()).description(f"String of {key}")
        
        ua = UserAgent().random
        response = requests.get(self.url, headers={'User-Agent': ua})
        soup = BeautifulSoup(response.content, 'html.parser')
        print("Soup created, extracting page data...")
        html = soup.prettify()
        html = clean_html(html).strip()

        try:
            res = b.ExtractPageData(list(self.names.keys()), html, {"tb": tb})
            print("Done extracting page data...")
            result = {}    
            for category in self.categories:
                method_result = getattr(res, category)
                method_result = method_result.strip() 
                self.result = result[category] = method_result
            return result          
        except BamlError as e:
            print(e)

    def filter_output(self, output):
        print("TypeBuilder created...")
        res = b.FilterPageData(list(self.names.keys()), output)
        res = b.EnsureResults(res, output)
        if len(res) != len(list(self.names.keys())):
            return self.retry()
        return res
    
    def retry(self):
        print("Retrying...")
        res = self.extract_content()
        output = ''
        if not res:
            return self.retry()
        
        for item in list(res.values()):
            output += item
        res = self.filter_output(output)
        if len(res) != len(list(self.names.keys())):
            return self.retry()
        return res
    
    def extract(self):
        res = self.extract_content()
        output = ''
        if not res:
            return self.retry()
        for item in list(res.values()):
            output += item
        res = self.filter_output(output)
        return res