from contentagregator import db
from contentagregator.modules.auth.models import User

class User_article(db.Model):
    __tablename__ = 'user_article'

    article_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False)
    content= db.Column(db.Text, unique=False)


class Article_categories(db.Model):
    __tablename__ = 'article_categories'

    category_id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(40), unique=True)


class Article_cooperators(db.Model):
    __tablename__ = 'article_cooperators'

    article_cooperator_id = db.Column(db.Integer, primary_key = True)
    article_id = db.Column(db.ForeignKey(User_article.article_id, ondelete='CASCADE'))
    article = db.relationship(User_article, foreign_keys=article_id, backref=db.backref('article_cooperators', cascade='all'))
    user_id = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
    article_category_id = db.Column(db.ForeignKey(Article_categories.category_id, ondelete='CASCADE'))
    article_category = db.relationship(Article_categories, foreign_keys=article_category_id, backref=db.backref('article_cooperators', cascade='all'))


class Article_attachments(db.Model):
    __tablename__ = 'article_attachments'
    
    attachment_id = db.Column(db.Integer, primary_key = True)
    article_id = db.Column(db.Integer, db.ForeignKey('user_article.article_id'))
    article = db.relationship("User_article", backref="article_attachment")
    file_name = db.Column(db.String(255))


class User_notes(db.Model):
    __tablename__ = 'user_notes'

    note_id = db.Column(db.Integer, primary_key = True)
    note_content = db.Column(db.Text, unique=False)
    user_id = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))