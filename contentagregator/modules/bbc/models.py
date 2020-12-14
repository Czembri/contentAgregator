from contentagregator import db
from datetime import datetime


class Bbc(db.Model):
    __tablename__ = "bbc_news"
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    scraped = db.Column(db.DateTime, default=datetime.utcnow)