import requests
import random
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
from typing import List, Dict
import time
from tqdm import tqdm
import csv

class WebsiteScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def get_top_websites(self) -> List[str]:
        """
        Get a list of popular websites. You could expand this list or 
        fetch from an API like Alexa/Similarweb.
        """
        popular_sites = []
        with open('websites.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                popular_sites.append(row[1].strip())

        return [f'https://www.{site}' for site in popular_sites]

    def get_random_pages(self, base_url: str, num_pages: int = 3) -> List[str]:
        """Get random internal pages from a website."""
        try:
            response = requests.get(base_url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a.get('href') for a in soup.find_all('a', href=True)]
            internal_links = [
                urljoin(base_url, link) for link in links
                if not link.startswith(('http', 'https')) or base_url in link
            ]
            return random.sample(internal_links, min(num_pages, len(internal_links)))
        except Exception as e:
            print(f"Error getting pages from {base_url}: {e}")
            return []

    def extract_interesting_elements(self, html: str) -> List[Dict]:
        """Extract interesting HTML patterns from the page."""
        soup = BeautifulSoup(html, 'html.parser')
        interesting_patterns = []

        # Extract forms
        for form in soup.find_all('form'):
            interesting_patterns.append({
                'type': 'form',
                'html': str(form),
                'context': 'Form element with inputs and structure'
            })

        # Extract navigation
        for nav in soup.find_all('nav'):
            interesting_patterns.append({
                'type': 'navigation',
                'html': str(nav),
                'context': 'Navigation structure'
            })

        # Extract article/content sections
        for article in soup.find_all(['article', 'section', 'main']):
            interesting_patterns.append({
                'type': 'content',
                'html': str(article),
                'context': 'Content structure'
            })

        # Extract headers
        for header in soup.find_all('header'):
            interesting_patterns.append({
                'type': 'header',
                'html': str(header),
                'context': 'Header structure'
            })

        # Extract interesting div patterns (with specific classes/ids)
        for div in soup.find_all('div', class_=True):
            if any(keyword in (div.get('class', []) + [div.get('id', '')]) for keyword in ['container', 'wrapper', 'grid', 'flex', 'card', 'modal']):
                interesting_patterns.append({
                    'type': 'component',
                    'html': str(div),
                    'context': f"Component with class: {' '.join(div.get('class', []))}"
                })

        return interesting_patterns

    def generate_questions(self, pattern: Dict) -> List[str]:
        """Generate relevant questions about the HTML pattern."""
        questions = [
            f"What is the structure and purpose of this HTML? \n{pattern['html']}",
            f"Analyze the semantic meaning and relationships between elements in this code: \n{pattern['html']}",
            f"What accessibility features or considerations are present in this HTML? \n{pattern['html']}",
            f"How would a browser render this HTML structure? Describe the visual hierarchy: \n{pattern['html']}",
            f"What are the key components and their purposes in this {pattern['type']} structure? \n{pattern['html']}"
        ]
        return questions

    def create_dataset(self, num_websites: int = 50, pages_per_site: int = 3) -> List[Dict]:
        """Create a dataset of HTML patterns from real websites."""
        dataset = []
        websites = self.get_top_websites()
        
        for website in tqdm(random.sample(websites, 50), desc="Scraping websites"):
            try:
                # Get random pages from the website
                pages = self.get_random_pages(website, pages_per_site)
                
                for page_url in pages:
                    try:
                        response = requests.get(page_url, headers=self.headers, timeout=10)
                        patterns = self.extract_interesting_elements(response.text)
                        
                        for pattern in patterns:
                            question = random.choice(self.generate_questions(pattern))
                            
                            dataset.append({
                                "messages": [
                                    {
                                        "role": "user",
                                        "content": question
                                    },
                                    {
                                        "role": "assistant",
                                        "content": f"This is {pattern['type']} HTML from {website}. {pattern['context']}"
                                        # Note: You'd want to use Mistral API here to generate better responses
                                    }
                                ],
                                "metadata": {
                                    "source_url": page_url,
                                    "pattern_type": pattern['type']
                                }
                            })
                    except Exception as e:
                        print(f"Error processing page {page_url}: {e}")
                    
                    time.sleep(1)  # Be nice to the servers
                    
            except Exception as e:
                print(f"Error processing website {website}: {e}")
        
        return dataset

def save_dataset(dataset: List[Dict], filename: str = "dataset.jsonl"):
    """Save dataset to JSONL file."""
    with open(filename, 'w', encoding='utf-8') as f:
        for example in dataset:
            f.write(json.dumps(example, ensure_ascii=False) + '\n')

# Usage
if __name__ == "__main__":
    scraper = WebsiteScraper()
    dataset = scraper.create_dataset(num_websites=10, pages_per_site=3)
    save_dataset(dataset)
    print(f"Generated dataset with {len(dataset)} examples")