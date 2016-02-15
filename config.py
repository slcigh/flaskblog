# -*- coding:utf8 -*-
# encoding = utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "hardtoguesss"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    WHOOSH_BASE = '/tmp/whoosh'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1931515@localhost/flaskdb2'
    SQLALCHEMY_POOL_RECYCLE = 5
    # from sae.const import (MYSQL_HOST, MYSQL_HOST_S, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)
    # SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' \
    #                             % (MYSQL_USER, MYSQL_PASS,
    #                                MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
