from contentagregator import app, db

from flask import render_template, Blueprint

communicates_module = Blueprint('communicates', __name__, url_prefix='/news/comm',  template_folder='templates', static_folder='static')

@app.route('/news/comm/test')
def test():
    return render_template('test.html')