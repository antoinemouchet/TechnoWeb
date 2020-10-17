from app import app
from flask import render_template, redirect, flash
from flask import url_for, request

# Dictionnaire avec toutes les données
users = {}

# example d'user
users["admin"] = {"name": "admin",
                  "dob" : "10-10-2010",
                  "password": "secret",
                  "group": "admin",
                  "tasks":{
                    '0': {"name": "Dodo", "description": "dormir", "deadline": "16-10-2020", "status": False},
                    '1': {"name": "TP techno web", "description": "Finir le tp", "deadline": "23-10-2020", "status": False}
                  }
}

# A task as the following format
# [name, id, state]
taskList = []

@app.route("/", methods=['GET'])
def todoList():

    unFinished = 0
    for task in taskList:
        if not task[2]:
            unFinished += 1

    return render_template("todoList.html", length = len(taskList), tasks = taskList, notDone = unFinished)


# Add a task
@app.route("/newTask", methods=['GET', 'POST'])
def newTask():
    if request.method == 'POST':
        newTask = request.form["task"]

        if newTask:
            # A task state is set to False as a basis.
            taskList.append([newTask, len(taskList), False])
        

        return redirect("/")

    return render_template("newTask.html")



#Delete item from todo, remove it from the list
@app.route("/remove/<int:taskID>", methods=['GET'])
def remove(taskID):

    if request.method == 'GET':

        # Make sure requested ID is in range if not the case, then redirect
        if taskID > len(taskList) or taskID < 1:
            return redirect("/")

        taskList.pop(taskID - 1)

        # Change identifier of each variable to match its position in the list
        index = 0
        for task in taskList:
            task[1] = index
            index += 1
    
    return redirect("/")

# Change state value of a task
@app.route("/changeState/<int:taskID>", methods=['GET'])
def changeState(taskID):
    
    if request.method == 'GET':

        # Make sure requested ID is in range if not the case, then redirect
        if taskID > len(taskList) or taskID < 1:
            return redirect("/")

        taskList[taskID - 1][2] = not taskList[taskID - 1][2]
        #print(taskList[taskID - 1][2])
    return redirect("/")


@app.route("/modify/<int:taskID>", methods=['POST', 'GET'])
def modify(taskID):
    
    # Make sure requested ID is in range if not the case, then redirect
    if taskID > len(taskList) or taskID < 1:
        return redirect("/")

    if request.method == 'POST':
        newName = request.form['newName']
    
        # Check newName is smthg
        if newName:
            taskList[taskID - 1][0] = newName
            return redirect("/")
    
    # New template for changing name of a task
    return render_template("modify.html", name=taskList[taskID - 1][0], taskID=taskID)

