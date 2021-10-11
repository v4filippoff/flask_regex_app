from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import User
login_manager = LoginManager(app)
login_manager.login_view = 'accounts.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from accounts.blueprint import accounts
app.register_blueprint(accounts, url_prefix='/accounts')

import views