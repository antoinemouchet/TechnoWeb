from flask import Flask
from config import Config
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
login_manager.login_message = "You can not access this page. Please log in to access this page."
login_manager.session_protection = "strong"
from app import routes
