from bs4 import BeautifulSoup
import requests
from GetContent import GetContent

class BuildSoup:
    def __init__(self, url, gc):
        self.url = url
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.content, 'html.parser')
        self.gc = gc

    def add_dynamic_methods(self, methods_list):
        try: 
            for method in methods_list:
                part = method['part']
                tag = method['tag']
                content = method['content']
                attributes = method['attributes']

                def dynamic_method(self, tag=tag, content=content, attributes=attributes):
                    elements = self.soup.find_all(tag, {attr['attribute']: attr['value'] for attr in attributes})
                    return [element.get_text() for element in elements if element.get_text().strip() == content]

                setattr(self, part.replace(" ", "_").lower(), dynamic_method.__get__(self))
        except Exception as e:
            print(e)
            print("Error adding dynamic methods to BuildSoup object.")
            print("Retrying...")
            self.gc.retry()
            