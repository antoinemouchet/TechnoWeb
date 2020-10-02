from app import app
from flask import render_template, redirect
from flask import url_for, request


@app.route("/", methods=['GET', 'POST'])
def todoList():

    # Read tasks from file
    taskFile = open("./app/static/todolist.txt", 'r')
    taskList = taskFile.readlines()
    taskFile.close()

    if request.method == 'POST':
        newTask = request.form["task"]

        if newTask:
            taskList.append(newTask + '\n')
            taskFile = open("./app/static/todolist.txt", 'w')
            taskFile.writelines(taskList)
            taskFile.close()
        else:
            return redirect("/")
        
    return render_template("todoList.html", length=len(taskList), tasks=taskList)

#Delete item from todo, remove it from the list
@app.route("/remove/<int:taskID>", methods=['GET'])
def remove(taskID):
    # Get list of tasks
    taskFile = open("./app/static/todolist.txt", 'r')
    taskList = taskFile.readlines()
    taskFile.close()

    if request.method == 'GET':
        taskList.pop(taskID - 1)
        taskFile = open("./app/static/todolist.txt", 'w')
        taskFile.writelines(taskList)
        taskFile.close()
    
    return redirect("/")
