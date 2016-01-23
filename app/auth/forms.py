# -*- coding:utf-8 -*-
# encoding=utf-8
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from app import db
from ..models import User
from app.auth.auth_config import REGCODE


class LoginForm(Form):
    login = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise ValidationError('Invalid user')

        if not user.verify_password(self.password.data):
            raise ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(username=self.login.data).first()


class RegisterForm(Form):
    username = StringField(
            validators=[DataRequired(), Length(1, 32), Regexp('^[_a-zA-Z0-9\u4e00-\u9fa5]+$', 0, "只能包含字母数字汉字或者下划线")])
    password = PasswordField(validators=[DataRequired(), EqualTo("password2", "Password must match")])
    password2 = PasswordField(validators=[DataRequired()])
    regcode = StringField(validators=[DataRequired()])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exist')

    def validate_regcode(self, field):
        if self.regcode.data != REGCODE:
            raise ValidationError('invalid REGCODE')
