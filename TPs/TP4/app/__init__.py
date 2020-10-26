from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Create the flask app
app = Flask(__name__)

# Config of the app
app.config.from_object(Config)

# Login
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
login_manager.login_message = "You can not access this page. Please log in to access this page."
login_manager.session_protection = "strong"

# Data base
db = SQLAlchemy(app)
from app import routes
