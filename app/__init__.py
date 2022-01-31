from flask import Flask
from flask_bootstrap import Bootstrap
from ..config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    from app.main import views
    from app.main import error

    return app

# bootstrap = Bootstrap(app)

# from app import views
# from app import error