from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class RegexTestForm(FlaskForm):
    regex_string = StringField('Regex string', validators=[DataRequired()])
    test_string = TextAreaField('Test string', validators=[DataRequired()])