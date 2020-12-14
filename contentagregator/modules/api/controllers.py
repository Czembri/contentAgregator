from flask import jsonify, Blueprint
import requests
from bs4 import BeautifulSoup
from contentagregator.config import SCRAP_URLS
from contentagregator import app, db
from contentagregator.modules.api.scrap import (
    interia, 
    gazeta, 
    rmf, 
    tvn_24,
    wp, 
    bbc,
    google,
    cnn
)

api_module = Blueprint('api', __name__, url_prefix='/api/v1')


def get_source(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    return soup

# english news 
@app.route('/api/v1/en/google')
def google_get():
    google_data = google()
    return jsonify(google_data)


@app.route('/api/v1/en/bbc')
def bbc_get():
    bbc_data = bbc()
    return jsonify(bbc_data)


@app.route('/api/v1/en/cnn')
def cnn_get():
    cnn_data = cnn()
    return jsonify(cnn_data)


# polish news

@app.route('/api/v1/pl/rmf')
def rmf_get():
    rmf_data = rmf()
    return jsonify(rmf_data)


@app.route('/api/v1/pl/interia')
def interia_get():
    interia_data = interia()
    return jsonify(interia_data)


@app.route('/api/v1/pl/gazeta')
def gazeta_get():
    gazeta_data = gazeta()
    return jsonify(gazeta_data)


# fix scraping for wp and tvn24

@app.route('/api/v1/pl/wp')
def wp_get():
    wp_data = wp()
    return jsonify(wp_data)


@app.route('/api/v1/pl/tvn24')
def tvn_24_get():
    tvn_24_data = wp()
    return jsonify(tvn_24_data)