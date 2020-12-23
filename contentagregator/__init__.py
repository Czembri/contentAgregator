from flask import Flask, render_template, session, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config.from_object('contentagregator.config.DevelopmentConfig')

db = SQLAlchemy(app)
assets = Environment(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

# endpoints that don't require logging in
allowedEndpoints = ('login', 'logout', None, 'register')

#register blueprints
from contentagregator.modules.api.controllers import api_module
from contentagregator.modules.bbc.controllers import bbc_module
from contentagregator.modules.auth.controllers import auth_module
from contentagregator.modules.about.controllers import about_module
from contentagregator.modules.google.controllers import google_module
from contentagregator.modules.communicates.controllers import communicates_module

app.register_blueprint(api_module)
app.register_blueprint(bbc_module)
app.register_blueprint(auth_module)
app.register_blueprint(communicates_module)
app.register_blueprint(about_module)
app.register_blueprint(google_module)


# API section
from contentagregator.modules.api import resources
api.add_resource(resources.UserRegistration, '/auth/register')
api.add_resource(resources.UserLogin, '/auth/login')
api.add_resource(resources.UserLogoutAccess, '/auth/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/auth/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

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
            session['logged_in'] == False and # not logged in
            (request.endpoint not in allowedEndpoints) and # not in allowed endpoits
            (request.endpoint.split('.')[-1] != 'static')  # not static file
    ):
        return redirect(url_for('login'))


#import assets
import contentagregator.assets