from flask import jsonify, Blueprint
import requests
from bs4 import BeautifulSoup
from contentagregator.config import SCRAP_URLS
from contentagregator import app, db
from contentagregator.modules.api.scrap import (
    interia, 
    gazeta, 
    rmf, 
    bbc,
    google,
    cnn
)
from flask_restful import Resource

api_module = Blueprint('api', __name__, url_prefix='/api/v1')


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

