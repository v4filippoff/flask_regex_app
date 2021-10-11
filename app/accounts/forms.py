from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=100)])
    remember = BooleanField('Remember', default=False)


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=100)])
    password_confirm = PasswordField('Password confirm', validators=[DataRequired(), Length(min=4, max=100)])