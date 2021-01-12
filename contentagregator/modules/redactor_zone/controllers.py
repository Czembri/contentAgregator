from contentagregator import app, db
from contentagregator.modules.redactor_zone.models import Article_categories, User_article, Article_cooperators, Article_attachments, User_notes
from contentagregator.modules.auth.models import User

from collections import defaultdict
import re
from datetime import datetime

from sqlalchemy import func
from flask import render_template, Blueprint, session, request, jsonify, flash, redirect, url_for

redactor_zone_module = Blueprint('redactor_zone', __name__, url_prefix='/redactor-zone', template_folder='templates', static_folder='static')


# no routes functions
def delete_html_tags(html_tag):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', html_tag)
    return cleantext


@app.route('/redactor-zone')
def redactor_zone_get_view():
    session['redactor'] = True
    user_id = session['user_id']
    articles_count = Article_cooperators.query.filter_by(user_id=user_id).count()
    latest_notes = User_notes.query.filter_by(
        user_id=user_id
        ).order_by(
            User_notes.note_id.desc()
            ).limit(3)
    return render_template(
        'redactor_zone.html', 
        articles_count=articles_count, 
        latest_notes=latest_notes)


@app.route('/redactor-zone/api/user-articles')
def redactor_zone_api_user_articles():
    user_id = session['user_id']
    user_articles = Article_cooperators.query.filter_by(user_id=user_id).all()
    serialized_articles = []
    for article in user_articles:
        article_cat = Article_categories.query.filter_by(
            category_id=article.article_category_id
            ).one_or_none()
        serialized_article = article.article.__dict__
        serialized_article['article_category'] = article_cat.category_name
        serialized_article.pop('_sa_instance_state', None)
        serialized_articles.append(serialized_article)
    return jsonify(serialized_articles)


@app.route('/redactor-zone/how-to-start')
def how_to_start():
    return render_template('how_to_start.html')


@app.route('/redactor-zone/user-article/<int:article_id>')
@app.route('/redactor-zone/create-an-article')
def create_an_article(article_id=None):
    user_article = None
    attachments=None
    if article_id is not None:
        user_article = Article_cooperators.query.filter_by(article_id=article_id).one_or_none()
        attachments = Article_attachments.query.filter_by(article_id=article_id).all()
    article_categories = Article_categories.query.all()
    categories = [category.category_id for category in article_categories]
    return render_template(
        'create_an_article.html', 
        categories=sorted(categories, key=int), 
        user_article=user_article, 
        attachments=attachments)


@app.route('/redactor-zone/articles')
def articles_view_get():
    user_id = session['user_id']
    user_articles = Article_cooperators.query.filter_by(user_id=user_id).all()
    return render_template('articles.html', user_articles=user_articles)


@app.route('/redactor-zone/create-an-article', methods=['POST'])
@app.route('/redactor-zone/user-article/<int:article_id>', methods=['POST'])
def create_an_article_post(article_id=None):
    user_id = session['user_id']
    filenames = []
    article_categories_form = request.form.get('check-category')
    article_title = request.form.get('title')
    article_content = delete_html_tags(request.form['trumbowyg'])

    if article_id is None:
        flash_message = 'The Article has been successfully added!'
        article = User_article(
            title = article_title,
            content=article_content,
            creation_time=datetime.utcnow()
        )

        db.session.add(article)
        db.session.commit()


        db.session.add(Article_cooperators(
                article_id=article.article_id,
                user_id=user_id,
                article_category_id=article_categories_form
            ))
        db.session.commit()
        flash(message=flash_message)
        
    else:
        article = User_article.query.filter_by(article_id=article_id).one_or_none()
        article.title = request.form.get('title')
        article.content = delete_html_tags(request.form['trumbowyg'])
        article.last_modified = datetime.utcnow()
        db.session.commit()

        article_coop = Article_cooperators.query.filter_by(article_id=article_id).one_or_none()
        article_coop.article_category_id = article_categories_form
        db.session.commit()
        flash('The Article has been successfully updated', 'success')

    for file in request.files.getlist('attachments[]'):
            if file.filename:
                filename = file.filename.split('.')[0]
                filenames.append(filename)
                attach = Article_attachments(
                    article_id=article.article_id,
                    file_name=filename
                )
                db.session.add(attach)
                db.session.commit()
        
    return redirect(url_for('articles_view_get'))


@app.route('/redactor-zone/delete-article/<int:article_id>', methods=['DELETE', 'POST'])
def delete_an_article(article_id):
    try:
        article = User_article.query.get(article_id)
        db.session.delete(article)
        db.session.commit()
        return redirect({'message':'Article deleted'})
    except Exception as err:
        return jsonify({'message':err})

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


@app.route('/redactor-zone/delete-note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        note = User_notes.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        return jsonify({'message':'Note deleted'})
    except Exception as err:
        return jsonify({'message':err})