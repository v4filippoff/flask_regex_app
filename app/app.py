from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    from models import User
    login_manager = LoginManager(app)
    login_manager.login_view = 'accounts.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from accounts.blueprint import accounts
    app.register_blueprint(accounts, url_prefix='/accounts')

    return app


app = create_app()
from views import *

if __name__ == '__main__':
    app.run('localhost', 8000)