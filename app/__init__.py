# encoding=utf-8
# coding:utf-8
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.login import LoginManager
from flask.ext.admin import Admin
from flask_admin.contrib import sqla

import flask.ext.whooshalchemy as whooshalchemy

login_manager = LoginManager()
# login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"

db = SQLAlchemy()
from app.models import Post
from app.admin import create_admin


def create_app(config_name):
    app = Flask(__name__)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # admin = Admin()
    # admin.add_view(sqla.ModelView(models.User, db.session))
    # admin.add_view(sqla.ModelView(models.Post, db.session))
    # admin.add_view(sqla.ModelView(models.Role, db.session))
    # admin.init_app(app)



    db.init_app(app)
    login_manager.init_app(app)

    create_admin(app, db)
    whooshalchemy.whoosh_index(app, Post)
    return app
