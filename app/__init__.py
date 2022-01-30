from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options

app = Flask(__name__,instance_relative_config= True)

app.config.from_object(config_options['development'])
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

from app import views
from app import error