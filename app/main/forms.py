# encoding=utf-8
# coding: utf8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(Form):
    title = StringField("title", validators=[DataRequired()])
    body = StringField("body", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])
