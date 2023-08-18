# Import the Flask class from the flask module
from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Import the 'routes' module from the 'app' package
from app import routes

