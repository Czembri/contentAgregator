from app import db
from flask import Blueprint

models = Blueprint('models', __name__)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(60), nullable=False)
    lname = db.Column(db.String(60), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    def __init__(self, fname, lname, country, content):
        self.fname = fname
        self.lname = lname
        self.country = country
        self.content = content
