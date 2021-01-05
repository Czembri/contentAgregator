from contentagregator import db

# class User_article(db.Model):
#     __tablename__ = 'user_article'

#     article_id = db.Column(db.Integer, primary_key = True)
#     user_id = db.Column(db.ForeignKey(User.id, ondelete='CASCADE'))
#     user_id = db.relationship(User, foreign_keys=user_id, backref=db.backref('article_owner', cascade='all'))
#     category = db.Column(db.String(120), unique = True, nullable = False)
#     title = db.Column(db.String(120), nullable = False)
#     content= db.Column(db.String(40), unique=True)


class Article_categories(db.Model):
    __tablename__ = 'article_categories'

    category_id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(40), unique=True)