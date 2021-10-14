from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class RegexMatchForm(FlaskForm):
    regex_string = StringField('Regex string', validators=[DataRequired()])
    test_string = TextAreaField('Test string', validators=[DataRequired()])


class RegexSubstitutionForm(RegexMatchForm):
    substitution_string = StringField('Substituion string')


class RegexSaveForm(FlaskForm):
    regex_name = StringField('Regex field', validators=[DataRequired(), Length(min=1, max=100)])
    regex_content = StringField('Regex content', validators=[DataRequired(), Length(min=1, max=1000)])
