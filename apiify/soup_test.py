from bs4 import BeautifulSoup
import requests

url = 'https://www.rottentomatoes.com/m/alien_romulus'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

elements = soup.find_all('div', {'class': 'score-wrap'})
print([element.get_text() for element in elements])