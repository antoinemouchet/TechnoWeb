# TP01 - Flask, Application ToDo

## **Requirements**
* python 3.7
* pip
* miniconda (*ou anaconda*)

## **Setup**
1. Clone the repository
2. Open a shell/command prompt
3. Use the following commands in the repository

```
conda env create -f environment.yml
```
```
pip install -r requirements.txt
```

!!!faq Note
    Those commands set up an isolated environment and download the required packages for the application so that it does not mess up with other existing versions of python and packages.

## **Launch**
If you have done everything right, you should be all setup to launch the app.

Just a few more commands in the shell In the same directory as the toDo.py file.

!!!warning
    This may vary depending on your OS.

### _Windows_
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

### _UNIX_
```bash
export FLASK_APP=toDo.py
flask run
```


## **How to use ?**
### _Add a task_
* Enter the task in the "*Enter New Task*" text box
* Press Submit

### _Remove a task_
* Press the x next to the task you wish to remove.


## **Note**
When you close the app, task are saved inside the *todolist.txt* file located in the static folder. When you open the app, tasks written in this file are loaded and displayed along the new ones.