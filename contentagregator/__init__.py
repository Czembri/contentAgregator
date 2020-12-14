from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment


app = Flask(__name__)

app.config.from_object('contentagregator.config.DevelopmentConfig')

db = SQLAlchemy(app)
assets = Environment(app)

#register blueprints
from contentagregator.modules.api.controllers import api_module
from contentagregator.modules.bbc.controllers import bbc_module
from contentagregator.modules.auth.controllers import auth_module
from contentagregator.modules.communicates.controllers import communicates_module

app.register_blueprint(api_module)
app.register_blueprint(bbc_module)
app.register_blueprint(auth_module)
app.register_blueprint(communicates_module)

#import assets
import contentagregator.assets