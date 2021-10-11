from flask import Blueprint

from models import User


accounts = Blueprint('accounts', __name__, template_folder='templates', static_url_path='static')

@accounts.route('/')
def index():
    return 'Hello, Accounts!'