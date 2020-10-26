from app import app, db
from flask import render_template, redirect, flash
from flask import url_for, request
from flask_login import login_required, login_user, logout_user, current_user
import app.forms as af
import app.utils as au
import app.models as am
from config import *

@app.route("/", methods=['GET'])
@login_required
def todoList():

    # Get tasks of the current user
    taskList = am.Task.query.filter_by(owner=current_user.get_id()).all()

    # Compute tasks done/not done
    unFinished = 0
    for task in taskList:
        if not task.state:
            unFinished += 1

    return render_template("todoList.html", length = len(taskList), tasks = taskList, notDone = unFinished, permission=am.Group.query.filter_by(id=current_user.group).first().permission_level)


# Add a task
@app.route("/newTask", methods=['GET', 'POST'])
@login_required
def newTask():

    # Generate form.
    task_form = af.TaskForm()

    # Check entries are valid
    if task_form.validate_on_submit():

        user_id = current_user.id
        
        # Check if there is already a task
        newTask = am.Task(owner=user_id, name=task_form.taskName.data, state=False, description=task_form.description.data, deadline=task_form.deadline.data)

        db.session.add(newTask)
        db.session.commit()

        return redirect("/")

    return render_template("newTask.html", form=task_form, permission=am.Group.query.filter_by(id=current_user.group).first().permission_level)



#Delete item from todo, remove it from the list
@app.route("/remove/<int:taskID>", methods=['GET'])
@login_required
def remove(taskID):

    if request.method == 'GET':
        # Get tasks of the current user
        taskList = am.Task.query.filter_by(owner=current_user.get_id()).all()

        # Make sure requested ID is in range if not the case, then redirect
        if not au.check_task_in(taskList, taskID) or taskID < 1:
            return redirect("/")


        task_to_del = am.Task.query.filter_by(owner=current_user.get_id(), id=taskID).first()

        db.session.delete(task_to_del)
        db.session.commit()

    
    return redirect("/")

# Change state value of a task
@app.route("/changeState/<int:taskID>", methods=['GET'])
@login_required
def changeState(taskID):
    
    if request.method == 'GET':
        # Get tasks of the current user
        taskList = am.Task.query.filter_by(owner=current_user.get_id()).all()

        # Make sure requested ID is in range if not the case, then redirect
        if not au.check_task_in(taskList, taskID) or taskID < 1:
            return redirect("/")

        task_to_change = am.Task.query.filter_by(owner=current_user.get_id(), id=taskID).first()
        task_to_change.state = not task_to_change.state

        db.session.add(task_to_change)
        db.session.commit()
        
    return redirect("/")


@app.route("/modify/<int:taskID>", methods=['POST', 'GET'])
@login_required
def modify(taskID):
    
    # Get tasks of the current user
    taskList = am.Task.query.filter_by(owner=current_user.get_id()).all()

    # Make sure requested ID is in range if not the case, then redirect
    if not au.check_task_in(taskList, taskID) or taskID < 1:
        return redirect("/")

    task_form = af.TaskForm()

    task_to_change = am.Task.query.filter_by(owner=current_user.get_id(), id=taskID).first()

    # Check form entries are valid
    if task_form.validate_on_submit():

        # Modify task with new values.
        task_to_change.name = task_form.taskName.data
        task_to_change.description = task_form.description.data
        task_to_change.deadline = task_form.deadline.data 


        db.session.add(task_to_change)
        db.session.commit()

        return redirect("/")
    
    # New template for changing name of a task
    return render_template("modify.html", name=task_to_change.name, taskID=taskID, form=task_form, permission=am.Group.query.filter_by(id=current_user.group).first().permission_level)

@app.route("/login", methods=['POST', 'GET'])
def login():
    # User is already logged in
    if current_user.is_authenticated:
        return redirect("/")
    
    # Create login form object
    login_form = af.LoginForm()
    
    # Check that form is valid.
    if login_form.validate_on_submit():
        
        # Look for the user in the existing users.
        user = am.User.query.filter_by(username=login_form.username.data).first()

        if user:
            # Check account not blocked
            if not user.status:
                flash("Account blocked.", category="danger")
                return redirect("/login")

            # Check if password matches 
            if user.check_password(login_form.password.data):
                login_user(user)
                return redirect("/")
            else:
                flash("Wrong password.", category="danger")
                return redirect("/login")
        
        else:
            flash("Wrong username", category="danger")
            return redirect("/login")

    else:
        return render_template("login.html", form=login_form)


@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route("/register", methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect("/")
    
    register_form = af.RegisterForm()

    # Check that form is valid.
    if register_form.validate_on_submit():
        
        # Get Username given in form
        username = register_form.username.data

        # Look for the user in the existing users.
        if am.User.query.filter_by(username=username).first():
            flash("Username already used", category="danger")
            return redirect("/register")
        
        # Create user to add in db
        new_user = am.User(username=username, first_name=register_form.first_name.data, last_name=register_form.last_name.data, dob=register_form.dob.data, status=True, group=2)
        new_user.set_password(register_form.password.data)

        # Add user in database
        db.session.add(new_user)
        db.session.commit()


        flash("Account successfully created", category="success")
        return redirect("/login")

    else:
        return render_template("register.html", form=register_form)


@app.route("/admin", methods=['GET'])
@login_required
def admin():
    if current_user.group != 1:
        return redirect("/")
    
    else:
        return render_template("controlPannel.html", userList=am.User.query.all(), length=len(am.User.query.all()),  permission=am.Group.query.filter_by(id=current_user.group).first().permission_level)

@app.route("/changeGroup/<username>/<int:group>")
@login_required
def changeGroup(username, group):
    userList = am.User.query.all()
    # Check user exists and user trying to change role is admin
    if current_user.group != 1 or not au.check_user_in(userList, username):
        return redirect("/")

    user_to_change = am.User.query.filter_by(username=username).first()
    user_to_change.group = group

    db.session.add(user_to_change)
    db.session.commit()


    return redirect("/")

@app.route("/changeStatus/<username>/<int:status>")
@login_required
def changeStatus(username, status):
    userList = am.User.query.all()
    # Check user exists and user trying to change role is admin
    if current_user.group != 1 or not au.check_user_in(userList, username):
        return redirect("/")

    user_to_change = am.User.query.filter_by(username=username).first()


    if status == 0 :
        status = False
    else:
        status = True
    
    # Admin can't be blocked
    if user_to_change.group != 1:
        user_to_change.status = status

    db.session.add(user_to_change)
    db.session.commit()

    return redirect("/")