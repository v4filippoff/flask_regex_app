from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=40)])


class SignupForm(LoginForm):
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), Length(min=8, max=40)])