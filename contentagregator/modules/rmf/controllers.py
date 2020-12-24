from contentagregator import app
from contentagregator.modules.api.scrap import rmf

from flask import render_template, Blueprint

rmf_module = Blueprint('rmf', __name__, url_prefix='/news/rmf', template_folder='templates', static_folder='static')

@app.route('/news/rmf')
def rmf_get_view():
    return render_template('rmf.html')