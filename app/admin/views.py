# encoding=utf-8
# coding: utf8
from flask.ext.admin.contrib import sqla
from flask import url_for, redirect, request
from flask.ext.admin import expose, helpers
from flask.ext.login import current_user, login_user, logout_user
from wtforms import fields, widgets, validators
from app.auth.forms import *
from flask.ext.admin.base import AdminIndexView


class AdminCategoryView(sqla.ModelView):
    column_list = ('id', 'name')

    def is_accessible(self):
        return current_user.is_authenticated


class AdminTagView(sqla.ModelView):
    column_list = ('id', 'name')

    def is_accessible(self):
        return current_user.is_authenticated


class AdminUserView(sqla.ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += " ckeditor"
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


# Customized admin interface
class AdminPostView(sqla.ModelView):
    form_overrides = dict(body=CKTextAreaField)

    form_columns = ('title', 'category', 'tags', 'part', 'body', 'timestamp', 'not_hide')

    column_list = ('id', 'tags', 'category', 'title', 'body', 'timestamp', 'not_hide')

    column_default_sort = ('timestamp', True)

    form_args = dict(
            title=dict(validators=[validators.required()]),
            category=dict(validators=[validators.required()]),
            tags=dict(validators=[validators.required()]),
            body=dict(validators=[validators.required()])
    )

    def is_accessible(self):
        return current_user.is_authenticated

    create_template = 'admin/write.html'
    edit_template = 'admin/write.html'


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegisterForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)

            db.session.add(user)
            db.session.commit()

            login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))
