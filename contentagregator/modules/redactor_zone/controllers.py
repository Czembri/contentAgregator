from contentagregator import app, db

from flask import render_template, Blueprint, session, request, jsonify

redactor_zone_module = Blueprint('redactor_zone', __name__, url_prefix='/redactor-zone', template_folder='templates', static_folder='static')

@app.route('/redactor-zone')
def redactor_zone_get_view():
    session['redactor'] = True
    return render_template('redactor_zone.html')


@app.route('/redactor-zone/how-to-start')
def how_to_start():
    return render_template('how_to_start.html')


@app.route('/redactor-zone/create-an-article')
def create_an_article():
    return render_template('create_an_article.html')


@app.route('/redactor-zone/create-an-article', methods=['POST'])
def create_an_article_post():
    json_response = {}
    json_response['category'] = request.form.get('check-category')
    json_response['title'] = request.form.get('title')
    json_response['editor'] = request.form.get('editor')

    for file in request.files.getlist('attachments[]'):
        if file.filename:
            ext = file.filename.split('.')[-1]
            ext = ext.lower()
            json_response['file'] = filename

    return jsonify(json_response)
