from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    password_hash = db.Column(db.String(256))
    status = db.Column(db.Boolean, nullable=False)

    # Multiple tasks
    tasks = db.relationship("Task", backref="worker", lazy="dynamic")

    # Foreign key to group
    group = db.Column(db.Integer, db.ForeignKey("groups.id"))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Foreign key to users
    owner = db.Column(db.Integer, db.ForeignKey("users.id"))

    name = db.Column(db.String(80), nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text, nullable=True)
    deadline = db.Column(db.DateTime, nullable=False)


class Group(db.Model):

    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(20), unique=True, nullable=False)
    permission_level = db.Column(db.Integer, nullable=False)
    # A group has multiple members
    members = db.relationship("User", backref="member", lazy=True)

db.drop_all()
db.create_all()

# Create initial values of db
admin = Group(group_name="admin", permission_level=1)
normal = Group(group_name="normal", permission_level=0)

admin_user = User(username="admin", first_name="admin", last_name="admin", dob=datetime(2020, 10, 26), status=True, group=1)
admin_user.set_password("secret")

db.session.add(admin)
db.session.add(normal)
db.session.add(admin_user)

db.session.commit()


from app import login_manager

# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))