# TP04 - Flask, Application ToDo

## **Requirements**
* python 3.7 ([get it here](https://www.python.org/downloads/))
* pip
* miniconda (*or anaconda*) ([download available here](https://docs.conda.io/en/latest/miniconda.html))

## **Setup**
1. Clone the repository
2. Open a shell/command prompt
3. Use the following commands in the directory

```
conda env create -f environment.yml
```
```
pip install -r requirements.txt
```

### Note
Those commands set up an isolated environment and download the required packages for the application so that it does not mess up with other existing versions of python and packages.

## **Launch**
If you have done everything right, you should be ready to launch the app.

Just a few more commands to type in the shell in the same directory as the toDo.py file.

First, you have to activate the conda environment you just created
```
conda activate [environmentName]
```

### Warning
This may vary depending on your OS.

### Windows
#### **Powershell**
```ps
$env:FLASK_APP=./toDo.py 
flask run
```
#### **Command prompt**
```cmd
set FLASK_APP=toDo.py
flask run
```

### UNIX
```bash
export FLASK_APP=toDo.py
flask run
```


## **How to use ?**

### _Create a new account_
* Press Register and fill in the boxes
* Press Submit
  
### _Log In_
* Enter your username and password
* Press Submit

### _See your tasks_
* Click on "Home" in the navigation bar.

### _Add a task_
* Click on "New task" in the navigation bar
* Enter the task in the "*Enter New Task*" text box
* Add a deadline (YYYY-MM-DD)
* The description is optionnal
* Press Submit

### _Remove a task_
* Press the bin next to the task you wish to remove.

### _Edit a task_
* Press the pen next to the task you wish to edit
* Enter the new name of the task in the text box.
* Press Submit

### _Mark a task as done or not done_
* Press the check box icon next to the corresponding task.


## **Admin Guide**
If you are an admin, you have access to the control pannel.

### _Control Pannel_
The available options here are:
* Block/unblock an user
* Promote/demote an user

#### _Block - Unblock_
* Click on the corresponding lock icon next to the username of the person to block/unblock.

#### _Promote - Demote_
* Click on the colored arrow next to the actual grade of the username of the person to promote/demote

## **Note**
If a task is done, its name is crossed.
