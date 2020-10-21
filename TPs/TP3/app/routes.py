from app import app
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
    taskList = users[current_user.get_username()]["tasks"]

    # Compute tasks done/not done
    unFinished = 0
    for task in taskList:
        if not task[2]:
            unFinished += 1

    return render_template("todoList.html", length = len(taskList), tasks = taskList, notDone = unFinished)


# Add a task
@app.route("/newTask", methods=['GET', 'POST'])
@login_required
def newTask():

    # Generate form.
    task_form = af.TaskForm()

    # Check entries are valid
    if task_form.validate_on_submit():

        username = current_user.get_username()
        newTask = au.create_task(task_form.taskName.data, task_form.deadline.data, task_form.description.data)
        au.add_task(users, username, newTask)

        return redirect("/")

    return render_template("newTask.html", form=task_form)



#Delete item from todo, remove it from the list
@app.route("/remove/<int:taskID>", methods=['GET'])
@login_required
def remove(taskID):

    if request.method == 'GET':
         # Get tasks of the current user
        taskList = users[current_user.get_username()]["tasks"]

        # Make sure requested ID is in range if not the case, then redirect
        if taskID > len(taskList) or taskID < 1:
            return redirect("/")

        users[current_user.get_username()]["tasks"].pop(taskID - 1)

    
    return redirect("/")

# Change state value of a task
@app.route("/changeState/<int:taskID>", methods=['GET'])
@login_required
def changeState(taskID):
    
    if request.method == 'GET':
         # Get tasks of the current user
        taskList = users[current_user.get_username()]["tasks"]

        # Make sure requested ID is in range if not the case, then redirect
        if taskID > len(taskList) or taskID < 1:
            return redirect("/")

        users[current_user.get_username()]["tasks"][taskID - 1][2] = not taskList[taskID - 1][2]
        
    return redirect("/")


@app.route("/modify/<int:taskID>", methods=['POST', 'GET'])
@login_required
def modify(taskID):
    
     # Get tasks of the current user
    taskList = users[current_user.get_username()]["tasks"]

    # Make sure requested ID is in range if not the case, then redirect
    if taskID > len(taskList) or taskID < 1:
        return redirect("/")

    task_form = af.TaskForm()

    # Check form entries are valid
    if task_form.validate_on_submit():

        # Modify task with new values.
        users[current_user.get_username()]["tasks"][taskID - 1][0] = task_form.taskName.data
        users[current_user.get_username()]["tasks"][taskID - 1][1] = task_form.description.data
        users[current_user.get_username()]["tasks"][taskID - 1][3] = task_form.deadline.data 

        return redirect("/")
    
    # New template for changing name of a task
    return render_template("modify.html", name=taskList[taskID - 1][0], taskID=taskID, form=task_form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    # User is already logged in
    if current_user.is_authenticated:
        return redirect("/")
    
    # Create login form object
    login_form = af.LoginForm()
    
    # Check that form is valid.
    if login_form.validate_on_submit():
        
        # Generate only once the list of users
        userList = users.keys()

        # Get Username given in form
        username = login_form.username.data

        # Look for the user in the existing users.
        user_found = au.find_user(userList, username)

        if user_found:
            if not users[username]["status"]:
                flash("Account blocked.", category="danger")
                return redirect("/login")

            # Check if password matches and account not blocked
            if login_form.password.data == users[username]["password"]:
                user = am.User(username)
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
        
        # Generate only once the list of users
        userList = users.keys()

        # Get Username given in form
        username = register_form.username.data

        # Look for the user in the existing users.
        user_found = au.find_user(userList, username)

        if user_found:
            flash("Username already used", category="danger")
            return redirect("/register")
        
        au.add_user(users, username, register_form.first_name.data, register_form.last_name.data, register_form.dob.data, register_form.password.data)
        flash("Account successfully created", category="success")
        return redirect("/login")

    else:
        return render_template("register.html", form=register_form)


@app.route("/admin", methods=['GET'])
@login_required
def admin():
    if current_user.get_group() != "admin":
        return redirect("/")
    
    else:
        return render_template("controlPannel.html", data=users, userList=users.keys(), length=len(users.keys()))

@app.route("/changeGroup/<username>/<group>")
@login_required
def changeGroup(username, group):
    # Check user exists and user trying to change role is admin
    if current_user.get_group() != "admin" or username not in users.keys():
        return redirect("/")


    au.change_user_group(users, username, group)
    return redirect("/")

@app.route("/changeStatus/<username>/<int:status>")
@login_required
def changeStatus(username, status):
    # Check user exists and user trying to change role is admin
    if current_user.get_group() != "admin" or username not in users.keys():
        return redirect("/")

    if status == 0 :
        status = False
    else:
        status = True
    
    au.un_block_user(users, username, status)
    return redirect("/")