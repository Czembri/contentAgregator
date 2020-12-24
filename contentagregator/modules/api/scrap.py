from bs4 import BeautifulSoup, NavigableString, Tag
import requests
from datetime import date
from contentagregator import db
from contentagregator.config import SCRAP_URLS


class Scrap:
    today = date.today()
    def __init__(self, tag, tag_class, name):
        self.tag = tag
        self.tag_class = tag_class
        self.name = name
    
    def scrap_data(self, data, soup):
        news = soup.find_all(self.tag, self.tag_class)
        for i in news:
            data += [
                    {
                        'Description':i.get_text(),
                        'Source':self.name,
                        'Scraped':self.today
                    }
                ]

    def scrap_data_en(self, data, soup):
        i = 1
        news = soup.find_all(self.tag)[1:6]
        for content in news:
            a = soup.find_all('a', class_=self.tag_class)[i]
            data += [
                    {
                        'Description':content.getText().split(','),
                        'Source':self.name,
                        'Scraped':self.today,
                        'Link': a['href']
                    }
                ]            
            i += 1
    

def get_source(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    return soup



def interia():
    data = []
    url = SCRAP_URLS['interia']
    soup = get_source(url)
    scrap = Scrap('a', 'tile-magazine-title-url', 'Interia').scrap_data(data, soup)
    return data

    

def wp():
    data = []
    url = SCRAP_URLS['wp']
    soup = get_source(url)
    scrap = Scrap('div', 'zb8eqt-1 gPSBdI', 'WP').scrap_data(data, soup)  
    return data


def gazeta():
    data = []
    url = SCRAP_URLS['gazeta']
    soup = get_source(url)
    news = soup.find_all('h2')
    for i in news:
        for a in i:
            if isinstance(a, NavigableString):
                continue
            if isinstance(a, Tag):
                data += [
                    {
                        'Description':a.get_text(),
                        'Source':'Gazeta.pl',
                        'Scraped':date.today()
                    }
                ]
    return data


def tvn_24():
    data = []
    url = SCRAP_URLS['tvn24']
    soup = get_source(url)
    scrap = Scrap('h2', 'heading article-title', 'TVN24').scrap_data(data, soup)
    return data


def rmf():
    data = []
    url = SCRAP_URLS['rmf']
    soup = get_source(url)
    news = soup.find_all('div', class_='titleContainer')
    counter = 0
    for i in news:
        for a in i:
            if isinstance(a, NavigableString):
                continue
            if isinstance(a, Tag):
                link = [str(link) for link in a if 'href' in str(link)]
                data += [
                    {
                        'Description':a.get_text().rstrip(),
                        'Link': link,
                        'Source':'RMF24',
                        'Scraped':date.today()
                    }
                ]

    return data


def bbc():
    data = []
    url = SCRAP_URLS['bbc']
    soup = get_source(url)
    scrap = Scrap('h3', 'gs-c-promo-heading', 'BBC').scrap_data_en(data, soup)
    return data
 

def google():
    data = []
    url = SCRAP_URLS['google']
    soup = get_source(url)

    for content_goo in soup.find_all('a', class_='DY5T1d')[0:5]:
        google_content = content_goo.getText().split(',')
        next_ = soup.find_all('article')[0]
        a_ = next_.find('a')
        data += [
                    {
                        'Description': google_content,
                        'Source':'Google',
                        'Scraped':date.today(),
                        'Link':a_['href']
                    }
                ]
    return data


def cnn():
    data = []
    url = SCRAP_URLS['cnn']
    soup = get_source(url)
    
    article_1 = soup.find('h3', class_="cd__headline").a
    data += [
                    {
                        'Description': str(article_1),
                        'Source':'CNN',
                        'Scraped':date.today(),
                        'Link':article_1['href']
                    }
                ]
    i=1
    for content_cnn in soup.find_all('span', class_='cd__headline-text')[0:5]:
        cnn_content = content_cnn.getText().split(',')
        next_link = soup.find_all('h3', class_="cd__headline")[i]
        a_ = next_link.find('a')
        data += [
                    {
                        'Description': str(cnn_content),
                        'Source':'CNN',
                        'Scraped':date.today(),
                        'Link':a_['href']
                    }
                ]
        i += 1
    return data
