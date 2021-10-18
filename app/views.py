import re

from flask import request, render_template, redirect, url_for, abort
from flask_login import login_required, current_user

from app import app, db
from forms import RegexMatchForm, RegexSubstitutionForm, RegexSaveForm
from models import Regex, User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/match/', methods=['GET', 'POST'])
def match():
    form = RegexMatchForm()

    if form.validate_on_submit():
        regex_string = form.regex_string.data
        test_string = form.test_string.data

        # В ответ на ajax запрос возвращаем json объект с совпадениями
        return {
            'matches': re.findall(regex_string, test_string),
        }

    return render_template('match.html', form=form)


@app.route('/substitution/', methods=['GET', 'POST'])
def substitution():
    form = RegexSubstitutionForm()

    if form.validate_on_submit():
        regex_string = form.regex_string.data
        test_string = form.test_string.data
        substitution_string = form.substitution_string.data

        # В ответ на ajax запрос возвращаем json объект с совпадениями
        return {
            'sub_result': re.sub(regex_string, substitution_string, test_string),
        }

    return render_template('substitution.html', form=form)


@app.route('/save_regex/', methods=['GET', 'POST'])
@login_required
def save_regex():
    regex_string = request.args.get('regex_string')

    form = RegexSaveForm(regex_content=regex_string)

    if form.validate_on_submit():
        regex_name = form.regex_name.data
        regex_content = form.regex_content.data

        new_regex = Regex(name=regex_name, content=regex_content, user_id=current_user.id)
        db.session.add(new_regex)
        db.session.commit()

        return redirect(url_for('profile', username=current_user.username))
    
    return render_template('save_regex.html', form=form)


@app.route('/profile/<username>/')
def profile(username):
    user = User.query.filter_by(username=username).first()

    if user:
        return render_template('profile.html', user=user)
    else:
        abort(404)


@app.route('/delete_regex/<int:regex_id>/', methods=['GET', 'POST'])
@login_required
def delete_regex(regex_id):
    regex = Regex.query.filter_by(id=regex_id).first()

    if not regex:
        abort(404)
        
    if regex.user_id == current_user.id:
        if request.method == 'POST':
            db.session.delete(regex)
            db.session.commit()
            return redirect(url_for('profile', username=current_user.username))
        else:
            return render_template('delete_regex.html', regex=regex)
    else:
        abort(403)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html')