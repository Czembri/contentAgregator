from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from sassutils.wsgi import SassMiddleware
from flask_seeder import FlaskSeeder
from flask_language import Language, current_language
from celery import Celery

app = Flask(__name__)

app.debug=True
app.config.from_object('contentagregator.config.DevelopmentConfig')

db = SQLAlchemy(app)
assets = Environment(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)
mail = Mail(app)
seeder = FlaskSeeder(app, db)
lang = Language(app)

# celery setup
def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)

# scss setup
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'contentagregator': ('static/sass', 'static/css/compiled', '/static/css/compiled', False)
})

# endpoints that don't require logging in
allowedEndpoints = (
    'login',
    'logout', 
    None, 
    'register',
    'contact_form_view',
    'contact_form_post',
    'user_login_api'
    )

#register blueprints
from contentagregator.modules.api.controllers import api_module
from contentagregator.modules.bbc.controllers import bbc_module
from contentagregator.modules.cnn.controllers import cnn_module
from contentagregator.modules.auth.controllers import auth_module
from contentagregator.modules.about.controllers import about_module
from contentagregator.modules.google.controllers import google_module
from contentagregator.modules.communicates.controllers import communicates_module
from contentagregator.modules.contact.controllers import contact_module
from contentagregator.modules.redactor_zone.controllers import redactor_zone_module
from contentagregator.modules.redactor_zone_forum.controllers import redactor_zone_forum_module

app.register_blueprint(api_module)
app.register_blueprint(bbc_module)
app.register_blueprint(cnn_module)
app.register_blueprint(auth_module)
app.register_blueprint(communicates_module)
app.register_blueprint(about_module)
app.register_blueprint(google_module)
app.register_blueprint(contact_module)
app.register_blueprint(redactor_zone_module)
app.register_blueprint(redactor_zone_forum_module)

# API section
from contentagregator.modules.api import resources
api.add_resource(resources.UserRegistration, '/api/auth/register')
api.add_resource(resources.UserLogin, '/api/auth/login')
api.add_resource(resources.UserLogoutAccess, '/api/auth/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/api/auth/logout/refresh')
api.add_resource(resources.TokenRefresh, '/api/token/refresh')
api.add_resource(resources.AllUsers, '/api/users')
api.add_resource(resources.SecretResource, '/api/secret')
api.add_resource(resources.Translations, '/api/translations')

# custom errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


@app.before_request
def before_request():
    if (
            not session.get('user_id') and # not logged in
            (request.endpoint not in allowedEndpoints) and # not in allowed endpoits
            (request.endpoint.split('.')[-1] != 'static')  # not static file
    ):
        return redirect(url_for('login'))


@lang.allowed_languages
def get_allowed_languages():
    return ['en', 'pl']


@lang.default_language
def get_default_language():
    return 'en'


@app.route('/api/language')
def get_language():
    return jsonify({
        'language': str(current_language),
    })


@app.route('/api/language', methods=['POST'])
def set_language():
    req = request.get_json()
    language = req.get('language', None)

    lang.change_language(language)

    return jsonify({
        'language': str(current_language),
    })


#import assets
import contentagregator.assets