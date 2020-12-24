from contentagregator import app, db

from flask import render_template, Blueprint, session

redactor_zone_module = Blueprint('redactor_zone', __name__, url_prefix='/redactor-zone', template_folder='templates', static_folder='static')

@app.route('/redactor-zone')
def redactor_zone_get_view():
    session['redactor'] = True
    return render_template('redactor_zone.html')