from contentagregator import db
from contentagregator.modules.auth.models import User

from datetime import datetime

class User_post(db.Model):
    __tablename__ = 'user_post'

    post_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False)
    content= db.Column(db.Text, unique=False)
    creation_time = db.Column(db.DateTime, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, default=datetime.utcnow)



class Post_response(db.Model):
    __tablename__ = 'post_response'

    response_id = db.Column(db.Integer, primary_key = True)
    post_id = db.Column(db.Integer, db.ForeignKey('user_post.post_id'))
    post = db.relationship("User_post", backref="post_response")
    user_id = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
    content = db.Column(db.Text, unique=False)
    creation_time = db.Column(db.DateTime, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, default=datetime.utcnow)


class Post_groups(db.Model):
    __tablename__='post_groups'

    group_id = db.Column(db.Integer, primary_key = True)
    group_name = db.Column(db.String(255), nullable=False, unique=True)
    creation_time = db.Column(db.DateTime, default=datetime.utcnow)


class Post_cooperators(db.Model):
    __tablename__ = 'post_cooperators'

    post_cooperator_id = db.Column(db.Integer, primary_key = True)
    post_id = db.Column(db.ForeignKey(User_post.post_id, ondelete='CASCADE'))
    post = db.relationship(User_post, foreign_keys=post_id, backref=db.backref('post_cooperators', cascade='all'))
    user_id = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
    post_group_id = db.Column(db.ForeignKey(Post_groups.group_id, ondelete='CASCADE'))
    post_group = db.relationship(Post_groups, foreign_keys=post_group_id, backref=db.backref('post_cooperators', cascade='all'))


class Post_attachments(db.Model):
    __tablename__ = 'post_attachments'

    attachment_id = db.Column(db.Integer, primary_key = True)
    post_id = db.Column(db.Integer, db.ForeignKey('user_post.post_id'))
    post = db.relationship("User_post", backref="post_attachment")
    file_name = db.Column(db.String(255))
    creation_time = db.Column(db.DateTime, default=datetime.utcnow)



