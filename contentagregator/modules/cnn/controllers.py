from contentagregator import app, db

from flask import render_template, Blueprint

cnn_module = Blueprint('cnn', __name__, url_prefix='/news/cnn',  template_folder='templates', static_folder='static')

@app.route('/news/cnn')
def cnn_get_view():
    return render_template('cnn.html')