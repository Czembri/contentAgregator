from contentagregator import app, db
from contentagregator.modules.auth.models import User
from contentagregator.modules.redactor_zone_forum.models import (
    Post_groups,
    Post_attachments,
    User_post, 
    Post_cooperators,
    Post_response)

from datetime import datetime
from flask import render_template, Blueprint, session, request, jsonify, flash, redirect, url_for

redactor_zone_forum_module = Blueprint('redactor_zone_forum', __name__, url_prefix='/redactor-zone/forum', template_folder='templates', static_folder='static')


@app.route('/redactor-zone/forum')
def redactor_zone_forum_main_get():
    return render_template('forum-index.html')



@app.route('/redactor-zone/forum/create-post')
def redactor_zone_forum_create_post_get():
    user_id = session['user_id']
    user = User.query.get(user_id)
    return render_template('forum-create.html', user=user)


@app.route('/redactor-zone/forum/create-post', methods=['POST'])
@app.route('/redactor-zone/forum/edit-post/<int:post_id>', methods=['PUT'])
def redactor_zone_forum_create_post_post(post_id=None):
    user_id = session['user_id']
    post_group = request.form.get('post_groups')
    post_title = request.form.get('post_title')
    post_content = request.form.get('post_content')
    now = datetime.utcnow()
    filenames = []

    if post_group is None:
        post_group = 1
    elif Post_groups.query.filter_by(group_name=post_group).one_or_none() is None:
        post_group_db = Post_groups(
            group_name=post_group,
            creation_time=now
        )
        db.session.add(post_group_db)
        db.session.commit()
    else:
        post_group_db = Post_groups.query.filter_by(group_name=post_group).one_or_none()

    if post_id is None:
        post = User_post(
            title=post_title,
            content=post_content,
            creation_time=now
        )

        db.session.add(post)
        db.session.commit()


        post_coop = Post_cooperators(
            post_id=post.post_id,
            user_id=user_id,
            post_group_id=post_group_db.group_id if post_group_db.group_id else post_group
        )

        db.session.add(post_coop)
        db.session.commit()

    for file in request.files.getlist('post_attachments[]'):
            if file.filename:
                filename = file.filename.split('.')[0]
                filenames.append(filename)

                attachment = Post_attachments(
                    post_id=post.post_id,
                    file_name=filename,
                    creation_time=now
                )

                db.session.add(attachment)
                db.session.commit()

    return jsonify({
        'post_id':post.post_id,
        'info':{
            'title':post.title,
            'content':post.content,
            'creation_time':post.creation_time,
        },
        'user_id':post_coop.user_id,
        'post_group_id' :post_coop.post_group_id,
        'filenames':filenames
    })


@app.route('/redactor-zone/forum/show-post/<int:post_id>')
def redactor_zone_forum_show_post(post_id):
    user_id = session['user_id']
    post = Post_cooperators.query.filter_by(post_id=post_id).first()
    creation_time = datetime.strftime(post.post.creation_time, '%Y-%b-%d %H:%M:%S')
    modification_time = datetime.strftime(post.post.last_modified, '%Y-%b-%d %H:%M:%S')
    user = User.query.get(post.user_id)
    session_user = User.query.get(user_id)
    post_response = Post_response.query.filter_by(post_id=post_id).all()
    return render_template(
        'forum-post.html', 
        post=post, 
        user=user, 
        post_response=post_response,
        creation_time=creation_time,
        modification_time=modification_time,
        session_user=session_user
        )


@app.route('/redactor-zone/forum/add-comment/<int:post_id>', methods=['POST', 'PUT'])
def add_comment(post_id):
    user_id = session['user_id']
    now = datetime.utcnow()
    post_response = Post_response(
        post_id=post_id,
        user_id=user_id,
        content=request.form.get('add_commentary'),
        creation_time=now,
        last_modified=now
    )

    db.session.add(post_response)
    db.session.commit()

    return jsonify({
        'post_id':post_id,
        'user_id':user_id,
        'content':request.form.get('add_commentary'),
        'creation_time':now,
        'last_modified':now
    })