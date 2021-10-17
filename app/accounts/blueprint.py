from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from models import User
from accounts.forms import LoginForm, SignupForm


accounts = Blueprint('accounts', __name__, template_folder='templates', static_url_path='static')

@accounts.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('match'))
        else:
            flash('Incorrect login or password')

    return render_template('login.html', form=form)


@accounts.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        
        user = User.query.filter_by(username=username).first()

        if not user and password == confirm_password:
            new_user = User(username=username, password_hash=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('accounts.login'))
        else:
            flash('The user already exists or password and password confirmation don\'t match')

    return render_template('signup.html', form=form)


@accounts.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('match'))