from flask import Blueprint, render_template

from app import db
from models import User
from accounts.forms import LoginForm, SignupForm


accounts = Blueprint('accounts', __name__, template_folder='templates', static_url_path='static')

@accounts.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@accounts.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)


@accounts.route('/logout/')
def logout():
    return 'Logout'