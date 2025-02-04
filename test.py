from new_folder.dynamic_methods import dynamic_method

url = 'https://www.rottentomatoes.com/m/heart_eyes'
data = [{'part': 'Movie Title', 'tag': 'sr-text', 'content': 'Heart Eyes', 'attributes': []}, {'part': 'Tomatometer', 'tag': 'rt-text', 'content': '92%', 'attributes': [{'attribute': 'size', 'value': '1.375'}]}]

print(dynamic_method(url, data))