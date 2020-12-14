from contentagregator import app, db

from flask import render_template, Blueprint

bbc_module = Blueprint('bbc', __name__, url_prefix='/news/bbc',  template_folder='templates', static_folder='static')

@app.route('/news/bbc')
def bbc_get_view():
    return render_template('bbc.html')