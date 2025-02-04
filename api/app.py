
from flask import Flask, request, jsonify
from soup import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    result = {}

    key, value = get_movie_title()
    result[key] = value

    key, value = get_tomatometer()
    result[key] = value


    return jsonify(result)
