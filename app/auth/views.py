#encoding=utf-8
# coding: utf8
from flask import render_template, redirect, request, url_for, flash
from . import auth
from flask.ext.login import login_user, login_required, logout_user
from ..models import User
from .. import db
from .forms import LoginForm, RegisterForm

@auth.route('/admin/login')
def index():
    return render_template(url_for('admin.index'))
