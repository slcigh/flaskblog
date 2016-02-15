# encoding=utf-8
# coding:utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config
from flask.ext.login import LoginManager
import flask.ext.whooshalchemy as whooshalchemy

login_manager = LoginManager()
login_manager.login_view = "auth.login"

db = SQLAlchemy()
from app.models import Post
from app.admin import create_admin


def create_app():
    app = Flask(__name__)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    create_admin(app, db)
    whooshalchemy.whoosh_index(app, Post)
    return app
