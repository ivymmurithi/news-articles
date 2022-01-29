from flask import Flask
from .config import config_options

app = Flask(__name__,instance_relative_config= True)

app.config.from_object(config_options['development'])
app.config.from_pyfile('config.py')

from app import views