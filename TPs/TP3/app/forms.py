from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, DateField
from wtforms.validators import InputRequired, Length, EqualTo


# Form of a task
class TaskForm(FlaskForm):
    taskName = StringField("Name", render_kw={"placeholder":"Enter name of task"}, validators=[InputRequired()])
    description = TextAreaField("Description", render_kw={"placeholder":"Enter description of task"})
    deadline = DateField("Deadline",render_kw={"placeholder":"YYYY-MM-DD"}, validators=[InputRequired()])
    submit = SubmitField("Submit")


# Class to create password modification of an user.
class ChangePassword(FlaskForm):
    password = PasswordField("New Password", validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField("Repeat Password")
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    first_name = StringField("First name", validators=[InputRequired(), Length(min=3, max=10)])
    last_name = StringField("Last name", validators=[InputRequired(), Length(min=3, max=10)])
    dob = DateField("Date of birth", render_kw={"placeholder":"YYYY-MM-DD"}, validators=[InputRequired()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField("Repeat Password")
    submit = SubmitField("Submit")
