from contentagregator import app, db

from flask import render_template, Blueprint

auth_module = Blueprint('auth', __name__, url_prefix='/news',  template_folder='templates', static_folder='static')

@app.route('/news')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')