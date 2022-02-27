from flask import Flask
from app.config import DevConfig

# Initialization application
app = Flask(__name__)

#Setting up configuration
app.config.from_object(DevConfig)

from app import views