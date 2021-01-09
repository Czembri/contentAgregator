from contentagregator import app, db
from contentagregator.modules.redactor_zone.models import Article_categories, User_article, Article_cooperators, Article_attachments, User_notes
from contentagregator.modules.auth.models import User

from collections import defaultdict

from sqlalchemy import func
from flask import render_template, Blueprint, session, request, jsonify, flash, redirect, url_for

redactor_zone_module = Blueprint('redactor_zone', __name__, url_prefix='/redactor-zone', template_folder='templates', static_folder='static')

@app.route('/redactor-zone')
def redactor_zone_get_view():
    session['redactor'] = True
    user_id = session['user_id']
    articles_count = Article_cooperators.query.filter_by(user_id=user_id).count()
    return render_template('redactor_zone.html', articles_count=articles_count)

@app.route('/redactor-zone/api/user-articles')
def redactor_zone_api_user_articles():
    user_id = session['user_id']
    user_articles = Article_cooperators.query.filter_by(user_id=user_id).all()
    serialized_articles = []
    for article in user_articles:
        article_cat = Article_categories.query.filter_by(category_id=article.article_category_id).one_or_none()
        serialized_article = article.article.__dict__
        serialized_article['article_category'] = article_cat.category_name
        serialized_article.pop('_sa_instance_state', None)
        serialized_articles.append(serialized_article)
    return jsonify(serialized_articles)


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
    user_articles = Article_cooperators.query.filter_by(user_id=user_id).all()
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


@app.route('/redactor-zone/user-notes')
def user_notes():
    user_id = session['user_id']
    user_notes = User_notes.query.filter_by(user_id=user_id).all()
    return render_template('notes.html', user_id=user_id, user_notes=user_notes)


@app.route('/redactor-zone/user-notes/add-note', methods=['POST'])
def user_notes_post():
    user_id = session['user_id']
    note_content = request.form['note_content']
    note = User_notes(note_content=note_content, user_id=user_id)
    db.session.add(note)
    db.session.commit()
    return str(note.note_id)