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
    article = soup_goo.find('article').a
    link = article['href']

    article_2 = soup_goo.find_all('article')[1]
    a2 = article_2.find('a')
    link_2 = a2['href']

    article_3 = soup_goo.find_all('article')[1]
    a3 = article_3.find('a')
    link_3 = a3['href']

    article_4 = soup_goo.find_all('article')[1]
    a4 = article_4.find('a')
    link_4 = a4['href']

    article_5 = soup_goo.find_all('article')[1]
    a5 = article_5.find('a')
    link_5 = a5['href']
    return render_template('google.html', gc=gc, link=link, link_2=link_2, link_3=link_3, link_4=link_4, link_5=link_5)

@app.route('/bbc')
def bbc():
    url_bbc = 'https://www.bbc.com/news'
    response_bbc = requests.get(url_bbc).text
    soup_bbc = BeautifulSoup(response_bbc, 'html.parser')
    bbc = []
    for content_bbc in soup_bbc.find_all('h3')[1:6]:
        bbc_content = content_bbc.getText().split(',')
        bbc.append(bbc_content)

    a = soup_bbc.find('a', class_="gs-c-promo-heading")
    link = a['href']

    a2 = soup_bbc.find_all('a', class_="gs-c-promo-heading")[2]
    link_2 = a2['href']

    a3 = soup_bbc.find_all('a', class_="gs-c-promo-heading")[3]
    link_3 = a3['href']

    a4 = soup_bbc.find_all('a', class_="gs-c-promo-heading")[4]
    link_4 = a4['href']

    a5 = soup_bbc.find_all('a', class_="gs-c-promo-heading")[5]
    link_5 = a5['href']
    return render_template('bbc.html', bbc=bbc, link=link, link_2=link_2, link_3=link_3, link_4=link_4, link_5=link_5)

@app.route('/cnn')
def cnn():
    url_cnn = 'https://edition.cnn.com/world'
    response_cnn = requests.get(url_cnn).text
    soup_cnn = BeautifulSoup(response_cnn, 'html.parser')
    cnn = []
    for content_cnn in soup_cnn.find_all('span', class_='cd__headline-text')[0:5]:
        cnn_content = content_cnn.getText().split(',')
        cnn.append(cnn_content)

    article = soup_cnn.find('h3', class_="cd__headline").a
    link = article['href']

    article_2 = soup_cnn.find_all('h3', class_="cd__headline")[1]
    a = article_2.find('a')
    link_2 = a['href']

    article_3 = soup_cnn.find_all('h3', class_="cd__headline")[2]
    a2 = article_3.find('a')
    link_3 = a2['href']

    article_4 = soup_cnn.find_all('h3', class_="cd__headline")[3]
    a3 = article_4.find('a')
    link_4 = a3['href']

    article_5 = soup_cnn.find_all('h3', class_="cd__headline")[4]
    a4 = article_5.find('a')
    link_5 = a4['href']
    return render_template('cnn.html', cnn=cnn, link=link, link_2=link_2, link_3=link_3, link_4=link_4, link_5=link_5)

@app.route('/test')
def test():
    flash('Site under construction!', 'danger')
    return render_template('test.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')
