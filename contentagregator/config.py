import os
import configparser


#config
AVATAR_VALID_EXTENTIONS = ['jpg', 'png', 'jpeg']
ATTACHMENT_VALID_EXTENTIONS = AVATAR_VALID_EXTENTIONS + ['pdf', 'doc', 'docx']

#DATABASE CONFIGURATION SCOPE
config =configparser.ConfigParser()
with open('contentagregator/app_config.ini', 'r', encoding='utf-8') as f:
    config.read_file(f)
    db_config = {
        'login':config['DATABASE']['login'],
        'password':config['DATABASE']['password'],
        'url':config['DATABASE']['url'],
        'database':config['DATABASE']['db']
    }

    mail_config = {
        'usrnm':config['MAIL']['username'],
        'psswd':config['MAIL']['password'],
        'mail_default_sender':config['MAIL']['mail_default_sender'],
        'mail_sender':config['MAIL']['mail_sender'],
        'mail_receiver':config['MAIL']['mail_receiver']
    }
    secrets = {
        'secret_key':config['SECRETS']['secret_key'],
        'jwt_secret_key':config['SECRETS']['jwt_secret_key']
    }

    google_config = {
        'google_client_id':config['GOOGLE']['google_client_id'],
        'google_client_secret':config['GOOGLE']['google_client_secret']
    }


DB_URL = 'postgresql://{user}:{password}@{url}/{db}'.format(
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


MAIL_SENDER = mail_config['mail_sender']
MAIL_RECEIVER = mail_config['mail_receiver']

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets['secret_key'] 
    MAKO_TRANSLATE_EXCEPTIONS = False
    ASSETS_AUTO_BUILD = True
    JSON_SORT_KEYS = False
    ASSETS_DEBUG = False
    CORS_HEADERS = 'Content-Type'
    JWT_SECRET_KEY = secrets['jwt_secret_key']
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    GOOGLE_CLIENT_ID = google_config['google_client_id']
    GOOGLE_CLIENT_SECRET = google_config['google_client_secret']
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = DB_URL
    ENV = 'production'
    DEBUG = False
    TESTING = False
    # USE_X_SENDFILE = True # ?


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = DB_URL
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SEND_FILE_MAX_AGE_DEFAULT = 0  # forbid caching
    TEMPLATES_AUTO_RELOAD = True

    # using a test gmail account for now, to be changed for prod
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = mail_config['usrnm']
    MAIL_PASSWORD = mail_config['psswd']
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_SUPPRESS_SEND = False
    MAIL_DEFAULT_SENDER = mail_config['mail_default_sender']


class TestConfig(Config):
    SECRET_KEY = os.environ.get('FLASK_APP', 'run.py')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{url}/{db}'.format(
    user=db_config['login'], password=db_config['password'], url='172.17.0.3', db='redactorzone_test')
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False