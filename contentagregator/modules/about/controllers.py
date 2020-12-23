from contentagregator import app, db

from flask import render_template, Blueprint

about_module = Blueprint('about', __name__, url_prefix='/about',  template_folder='templates', static_folder='static')

@app.route('/about')
def about():
    return render_template('about.html')