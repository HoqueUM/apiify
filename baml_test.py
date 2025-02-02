# https://docs.boundaryml.com/guide/installation-language/python
from ollama import chat, ChatResponse
from baml_client import b


string = "This is an article called 'The worst movies ever' written by John Doe on 2022-01-01. It is about the worst movies ever. At the moment there is no content."
res = b.ExtractArticle(string)

print(res)