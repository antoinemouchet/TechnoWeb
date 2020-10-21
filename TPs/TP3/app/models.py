from flask_login import UserMixin
from config import *

class User (UserMixin):
    def __init__(self, id):
        self.id = id
        self.group = users[id]["group"]

    def get_username(self):
        return self.id

    def get_group(self):
        return self.group

from app import login_manager

# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)