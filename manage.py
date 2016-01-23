# -*- coding:utf8 -*-
# encoding=utf-8
# !/usr/bin/env python
import os
from app import create_app, db
from app.models import User
from flask.ext.script import Manager, Shell
from flask.ext.login import login_required

app = create_app(os.getenv("FLASK_CONFIG") or "default")
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
