# encoding=utf-8
# coding: utf8
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db
from . import login_manager
from jieba.analyse import ChineseAnalyzer

post_tags_table = db.Table('posts_tags', db.Model.metadata,
                           db.Column('posts_id', db.Integer, db.ForeignKey('posts.id')),
                           db.Column('tags_id', db.Integer, db.ForeignKey('tags.id'))
                           )


class Post(db.Model):
    __tablename__ = "posts"
    __searchable__ = ['title', 'body']
    __analyzer__ = ChineseAnalyzer()
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    part = db.Column(db.String(350))
    title = db.Column(db.Text)
    not_hide = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", backref=db.backref("posts", lazy="dynamic"))
   # tags_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
    tags = db.relationship("Tag", backref=db.backref("posts", lazy="dynamic"), secondary=post_tags_table)


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __str__(self):
        return self.name


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __str__(self):
        return self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
