import re

from flask import request, render_template, url_for, redirect

from app import app
from forms import RegexTestForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegexTestForm()

    if form.validate_on_submit():
        regex_string = form.regex_string.data
        test_string = form.test_string.data

        return {
            'maches': re.findall(regex_string, test_string),
        }

    return render_template('index.html', form=form)

