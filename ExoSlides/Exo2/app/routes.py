from app import app
from flask import render_template, redirect
from flask import url_for, request

@app.route("/", methods=['GET', 'POST'])
def process_request():

    # Dict to store values from form
    answers = {"name": None,
               "surname": None,
               "birthdate": None,
               "nationality": None}

    # Get data from form
    if request.method == 'POST':
        for key in answers.keys():
            answers[key] = request.form[key]
        
        # Check no value is None anymore
        if len(answers.values()) == 4:
            return render_template("process_response.html", name=answers["name"], surname=answers["surname"], birthdate=answers["birthdate"], nationality=answers["nationality"])
        else:
            return "Please go back and complete the form", 400
    else:
        return render_template("process_form.html")


