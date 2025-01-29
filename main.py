# https://docs.boundaryml.com/guide/installation-language/python
import openai
from baml_client import b
from baml_client.types import CountryCapital

client = openai.Client(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response = client.chat.completions.create(
    model="deepseek-r1",
    messages=[{'role': 'user', 'content': 'What is the capital of France?'}],
    temperature=0.7,
)
content = response.choices[0].message.content
print(content.split('>')[2].strip())

content = content.split('>')[2].strip()
country_info = b.ExtractCountryCapital(content)
print(f"Country: {country_info.country}")
print(f"Capital: {country_info.capital}")

