# -*- coding:utf8 -*-
# encoding = utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# from sae.const import (MYSQL_HOST, MYSQL_HOST_S, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)


class Config:
    SECRET_KEY = "hardtoguesss"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = "[Flasky]"
    FLASKY_MAIL_SENDER = "Flasky Admin <2721068406@qq.com>"
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN")
    WHOOSH_BASE = '/tmp/whoosh'
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    #   SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' \
    #                             % (MYSQL_USER, MYSQL_PASS,
    #                                MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1931515@localhost/flaskdb2'
    SQLALCHEMY_POOL_RECYCLE = 5


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-test.sqlite")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")


config = {"development": DevelopmentConfig,
          "testing": TestingConfig,
          "production": ProductionConfig,
          "default": DevelopmentConfig}
