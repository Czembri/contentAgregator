from contentagregator import app, db
from contentagregator.modules.auth.forms.auth_forms import LoginForm, RegisterForm
from contentagregator.modules.auth.models import User

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
    session
    )
import json
from werkzeug.security import generate_password_hash, check_password_hash

auth_module = Blueprint('auth', __name__, url_prefix='/news',  template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('choose_news.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate:
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if User.verify_hash(form.password.data, user.password):
                flash('You have successfully logged in.', "success")
                session['logged_in'] = True
                session['username'] = user.username
                session['user_id'] = user.id
                return redirect(url_for('index'))
            else:
                flash('Username or Password Incorrect', "error")
                return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = User.generate_hash(form.password.data)
        new_user = User(
            name = form.name.data, 
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
    session['logged_in'] = False
    return redirect(url_for('login'))