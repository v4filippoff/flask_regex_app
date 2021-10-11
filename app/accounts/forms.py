from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=100)])


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=100)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), Length(min=4, max=100)])