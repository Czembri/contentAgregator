from contentagregator import app, db

from flask import render_template, Blueprint

google_module = Blueprint('google', __name__, url_prefix='/news/google',  template_folder='templates', static_folder='static')

@app.route('/news/google')
def google_get_view():
    return render_template('google.html')