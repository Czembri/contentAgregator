from flask import Blueprint, render_template, redirect, url_for, flash
from app import app, db
import requests
from bs4 import BeautifulSoup

routes = Blueprint("routes", __name__, static_folder="static", template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/google')
def google():
    url_goo = 'https://news.google.com/?hl=en-US&gl=US&ceid=US:en'
    response_goo = requests.get(url_goo).text
    soup_goo = BeautifulSoup(response_goo, 'html.parser')
    gc = []
    for content_goo in soup_goo.find_all('a', class_='DY5T1d')[0:5]:
        google_content = content_goo.getText().split(',')
        gc.append(google_content)
    return render_template('google.html', gc=gc)

@app.route('/bbc')
def bbc():
    url_bbc = 'https://www.bbc.com/news'
    response_bbc = requests.get(url_bbc).text
    soup_bbc = BeautifulSoup(response_bbc, 'html.parser')
    bbc = []
    for content_bbc in soup_bbc.find_all('h3')[1:6]:
        bbc_content = content_bbc.getText().split(',')
        bbc.append(bbc_content)
    return render_template('bbc.html', bbc=bbc)

@app.route('/cnn')
def cnn():
    url_cnn = 'https://edition.cnn.com/world'
    response_cnn = requests.get(url_cnn).text
    soup_cnn = BeautifulSoup(response_cnn, 'html.parser')
    cnn = []
    for content_cnn in soup_cnn.find_all('span', class_='cd__headline-text')[0:5]:
        cnn_content = content_cnn.getText().split(',')
        cnn.append(cnn_content)
    for links in soup_cnn.find_all('a')[0:5]:
        link_1 = soup_cnn.find('div', class_="cd__content").a.get('href')

    return render_template('cnn.html', cnn=cnn, link=link_1)

@app.route('/test')
def test():
    flash('Site under construction!', 'danger')
    return render_template('test.html')
