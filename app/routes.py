from flask import Blueprint, render_template, redirect, url_for
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
    response_goo = requests.get(url).text
    soup_goo = BeautifulSoup(response_goo, 'html.parser')
    gc = []
    for content_goo in soup_goo.find_all('a', class_='DY5T1d'):
        google_content = content_goo.getText().split(',')
        gc.append(google_content)
    return render_template('google.html', gc=gc)

@app.route('/reddit')
def reddit():
    url_rd = 'https://www.reddit.com'
    response_rd = requests.get(url_rd).text
    soup_rd = BeautifulSoup(response_rd, 'html.parser')
    rd = []
    for content_rd in soup_rd.find_all('div', class_='_2SdHzo12ISmrC8H86TgSCp'):
        reddit_content = content_rd.getText().split(',')
        rd.append(reddit_content)
    return render_template('reddit.html', rd=rd)
