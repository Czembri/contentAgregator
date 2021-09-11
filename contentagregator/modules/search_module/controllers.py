from contentagregator import app
from flask import redirect, url_for, Blueprint


search_module = Blueprint('search',__name__, static_folder='static', template_folder='templates', url_prefix='/search')

@app.route('/search',methods=['POST'])
def search_form_post():
    return redirect(url_for('index'))