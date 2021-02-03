
from contentagregator import db
from passlib.hash import pbkdf2_sha256 as sha256

from datetime import datetime
import os


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    name= db.Column(db.String(40), unique=True)
    email = db.Column(db.String(70), unique=True)
    is_verified = db.Column(db.Integer, server_default="1")
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    articles = db.relationship("User_article", secondary="article_cooperators")
    posts = db.relationship("User_post", secondary="post_cooperators")
    avatar = db.Column(db.String(255))
    created = db.Column(db.DateTime, default=datetime.utcnow)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'id':x.id,
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), User.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}


    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)


    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class RevokedToken(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)


class Actions(db.Model):
    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key=True)
    action_name = db.Column(db.String(250))


class User_actions(db.Model):
    __tablename__ = 'user_actions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
    action_id = db.Column(db.ForeignKey(Actions.id, ondelete='CASCADE'))
    action = db.relationship(Actions, foreign_keys=action_id, backref=db.backref('actions', cascade='all'))
    action_name = db.Column(db.String(250))
    changed_on = db.Column(db.DateTime, default=datetime.utcnow)



    
