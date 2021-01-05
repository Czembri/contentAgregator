from contentagregator import app, db
from contentagregator.modules.redactor_zone.models import Article_categories

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
    article_categories = Article_categories.query.all()
    categories = [category.category_id for category in article_categories]
    return render_template('create_an_article.html', categories=sorted(categories, key=int))


@app.route('/redactor-zone/create-an-article', methods=['POST'])
def create_an_article_post():
    json_response = {}
    unpacked_categories = []
    article_categories_form = request.form.getlist('check-category')
    categories_to_display = [Article_categories.query.filter_by(category_id=x).all() for x in article_categories_form]
    for packed in categories_to_display:
        for to_unpack in packed:
            unpacked_categories.append(to_unpack.category_name)
    json_response['category'] = unpacked_categories
    json_response['title'] = request.form.get('title')
    json_response['editor'] = request.form['trumbowyg']
    json_response['file'] = [file.filename.split('.')[0] for file in request.files.getlist('attachments[]') if file.filename]

    return jsonify(json_response)
