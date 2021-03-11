from contentagregator import app, db, client
from contentagregator.modules.auth.forms.auth_forms import LoginForm, RegisterForm
from contentagregator.modules.auth.models import User
from contentagregator.tasks import run_scraper
from contentagregator.config import GOOGLE_DISCOVERY_URL, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET

from flask.views import MethodView
from flask import (
    render_template, 
    Blueprint, 
    g, 
    make_response, 
    redirect, 
    url_for, 
    jsonify, 
    flash, 
    request, 
    session,
    make_response
    )
import json
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import requests
import string
import random

auth_module = Blueprint('auth', __name__, url_prefix='/news',  template_folder='templates', static_folder='static')


@app.route('/')
def index():
    session['redactor'] = False
    return render_template('index.html')


@app.route('/news')
def news():
    run_scraper()
    return render_template('choose_news.html')


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


def password_generator():
    length = 10
    LETTERS = string.ascii_letters
    NUMBERS = string.digits  
    PUNCTUATION = string.punctuation 
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password


@app.route("/google-login/auth/callback")
def callback():
    code = request.args.get("code")
    
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url=request.base_url,
    code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    response = make_response(redirect(url_for('index')))
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        exists = User.query.filter_by(google_auth_id=unique_id).one_or_none()
        if exists is not None:
            session['logged_in']=True
            session['username'] = exists.username
            session['user_id'] = exists.id
            return response
        else:
            passw = password_generator()
            hashed_passw = User.generate_hash(passw)

            '''
            Send email with password to user!!!
            '''
            username = users_email.split('@')[0]
            user = User(
                google_auth_id=unique_id, username=username, email=users_email, avatar=picture, password=hashed_passw
            )
            db.session.add(user)
            db.session.commit()
            session['logged_in']=True
            session['user_id'] = user.id
            session['username'] = user.username
            return response
    else:
        return "User email not available or not verified by Google.", 400


@app.route("/google-login/auth")
def google_auth():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate:
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if User.verify_hash(form.password.data, user.password):
                flash('You have successfully logged in.', "success")
                user.last_seen = datetime.utcnow()
                db.session.commit()
                session['logged_in'] = True
                session['username'] = user.username
                session['user_id'] = user.id
                avatar = f'/letters/{user.username[0].upper()}.png' 
                session['avatar'] = avatar
                response = make_response(redirect(url_for('index')))
                return response
            else:
                flash('Username or Password Incorrect', "error")
                return redirect(url_for('login'))
        else: # just for development
            hashed_password = User.generate_hash(form.password.data)
            new_user = User(
                username=form.username.data,
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()

            session['logged_in'] = True
            session['username'] = new_user.username
            session['user_id'] = new_user.id
            response = make_response(redirect(url_for('login')))
            flash('User created', 'success')
            return response
    return render_template('login.html', form=form)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = User.generate_hash(form.password.data)
        new_user = User(
            first_name = form.first_name.data, 
            last_name = form.last_name.data, 
            username = form.username.data, 
            email = form.email.data, 
            password = hashed_password )
        db.session.add(new_user)
        db.session.commit()

        flash('You have successfully registered', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    user_id = session['user_id']
    user = User.query.get(user_id)
    user.last_seen = datetime.utcnow()
    db.session.commit()
    session.clear()
    return redirect(url_for('login'))


@app.route('/user/<string:username>/<int:user_id>')
def user(username,user_id):
    avatar = username[0].upper()
    user = User.query.get(user_id)
    return render_template('user.html', avatar=avatar, user=user)

@app.route('/user/<string:username>/<int:user_id>/update', methods=['PUT'])
def user_put(username,user_id):
    user_id_session = session['user_id']
    if user_id_session == user_id:
        user = User.query.get(user_id)
        if fullname:
            fullname = request.form.get('fullname').split()
        username =  request.form.get('username')
        email = request.form.get('email')
        if len(fullname) > 1:
            user.first_name = fullname[0]
            user.last_name = fullname[1]
        else:
            user.first_name = fullname[0]
        user.username = username
        user.email = email if email else ''

        db.session.commit()

    return jsonify(
        {'first_name':fullname[0] if len(fullname) > 1 else fullname[0],
        'last_name': fullname[1] if len(fullname) > 1 else '',
        'username': username,
        'email': email}
        )