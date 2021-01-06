from contentagregator import app, db
from contentagregator.modules.redactor_zone.models import Article_categories, User_article, Article_cooperators, Article_attachments
from contentagregator.modules.auth.models import User

from collections import defaultdict

from sqlalchemy import func
from flask import render_template, Blueprint, session, request, jsonify, flash, redirect, url_for

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


@app.route('/redactor-zone/articles')
def articles_view_get():
    user_id = session['user_id']
    user_articles = Article_cooperators.query.filter_by(user_id=user_id).group_by(Article_cooperators.article_id).all()
    return render_template('articles.html', user_articles=user_articles)


@app.route('/redactor-zone/create-an-article', methods=['POST'])
@app.route('/redactor-zone/article/<int:article_id>', methods=['POST'])
def create_an_article_post(article_id=None):
    user_id = session['user_id']
    json_response = {}
    unpacked_categories = []
    filenames = []
    article_categories_form = request.form.getlist('check-category')
    categories_to_display = [Article_categories.query.filter_by(category_id=x).all() for x in article_categories_form]
    json_response['category'] = unpacked_categories
    json_response['title'] = request.form.get('title')
    json_response['editor'] = request.form['trumbowyg']


  

    if article_id is None:
        flash_message = 'The Article has been successfully added!'
        article = User_article(
            title = request.form.get('title'),
            content = request.form['trumbowyg']
        )

        db.session.add(article)
        db.session.commit()

        for packed in categories_to_display:
            for to_unpack in packed:
                unpacked_categories.append(to_unpack.category_id)

        for ids in unpacked_categories:
            db.session.add(Article_cooperators(
                    article_id=article.article_id,
                    user_id=user_id,
                    article_category_id=ids
                ))
            db.session.commit()

        for file in request.files.getlist('attachments[]'):
            if file.filename:
                filename = file.filename.split('.')[0]
                filenames.append(filename)
                json_response['file'] = filenames
                attach = Article_attachments(
                    article_id=article.article_id,
                    file_name=filename
                )
                db.session.add(attach)
                db.session.commit()
    flash(message=flash_message)
    return redirect(url_for('articles_view_get'))
