from flask import Flask
from app.config import DevConfig

# Initialization application
app = Flask(__name__,instance_relative_config= True)


#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views