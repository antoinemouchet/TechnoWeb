from app import app
from flask import render_template, redirect
from flask import url_for, request

@app.route("/")
def hello():
        return "<h1> Hello World ciao! </h1>"

@app.route('/hello_world_one')
def hello_world_one():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>hello</title></head>
    <body><h1>Hello World One</h1></body>
    </html>""", 200

# Nom d'utilisateur, type pas spécifié
@app.route("/hello_world_two/<username>")
def hello_world_two(username):
    return "Hello {}".format(username)

# Exactement 8
@app.route("/hello_world_three/<string(length=8):username>")
def hello_world_three(username):
    return "Hello {}".format(username)

# Entre 4 et 8
@app.route("/hello_world_four/<string(minlength=4, maxlength=8):username>")
def hello_world_four(username):
    return "Hello {}".format(username)

# Nombre
@app.route("/hello_world_five/<int:userid>")
def hello_world_five(userid):
    return "Hello your user ID is: {:d}".format(userid)


@app.route("/hello_world_six")
def hello_world_six(name="", surname=""):
    name = request.args.get("name")
    surname = request.args.get("surname")
    return "You entered a query string with the name of {}{},\
        and request.args.get returned it as {}, of course!".format(name, surname, type(name).__name__)

@app.route("/hello_world_template")
def hello_world_template():
    return render_template("hello.html")

@app.route("/process_request", methods=['GET', 'POST'])
def process_request_function():
    if request.method == 'POST':
        _username = request.form["username"]
        if _username:
            return render_template("process_response.html", username=_username)
        else:
            return "Please go back and enter your name", 400
    else:
        return render_template("process_form.html")

