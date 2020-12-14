import os
import configparser


#DATABASE CONFIGURATION SCOPE
config =configparser.ConfigParser()
with open('contentagregator/db_config.ini', 'r', encoding='utf-8') as f:
    config.read_file(f)
    db_config = {
        'login':config['USER']['login'],
        'password':config['USER']['password'],
        'url':config['DATABASE']['url'],
        'database':config['DATABASE']['db']
}

DB_URL = 'mysql://{user}:{password}@{url}/{db}'.format(
    user=db_config['login'], password=db_config['password'], url=db_config['url'], db=db_config['database'])


SCRAP_URLS = {
    'google':'https://news.google.com/?hl=en-US&gl=US&ceid=US:en',
    'bbc':'https://www.bbc.com/news',
    'cnn':'https://edition.cnn.com/world',
    'interia':'https://fakty.interia.pl/polska',
    'wp':'https://www.wp.pl/',
    'gazeta':'https://wiadomosci.gazeta.pl/wiadomosci/0,0.html',
    'tvn24':'https://tvn24.pl/najnowsze/',
    'rmf':'https://www.rmf24.pl/fakty/polska'
}



class Config:
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # silence warning
    SECRET_KEY = 'SECRET_KEY'  # has to be changed on production
    OIDC_CLIENT_SECRETS = 'client_secrets.json'  # keycloak config file
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    MAKO_TRANSLATE_EXCEPTIONS = False
    ASSETS_AUTO_BUILD = True
    JSON_SORT_KEYS = False
    ASSETS_DEBUG = False
    CORS_HEADERS = 'Content-Type'




class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    # USE_X_SENDFILE = True # ?


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SEND_FILE_MAX_AGE_DEFAULT = 0  # forbid caching
    TEMPLATES_AUTO_RELOAD = True

    # using a test gmail account for now, to be changed for prod
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_SUPPRESS_SEND = False
    MAIL_DEFAULT_SENDER = 'gildartsft16@gmail.com'


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False