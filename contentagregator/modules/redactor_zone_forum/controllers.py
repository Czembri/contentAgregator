from contentagregator import app, db
from contentagregator.modules.auth.models import User

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