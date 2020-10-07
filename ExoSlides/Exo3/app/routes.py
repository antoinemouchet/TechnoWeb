from app import app
from flask import render_template, redirect
from flask import url_for, request
import os
from app.upload_file import allowed_file
from werkzeug.utils import secure_filename
from flask import send_from_directory


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

@app.route("/uploadfile", methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':

        # Check if there is a file in the form
        if "file" not in request.files:
            return redirect(request.base_url)

        
        # Get the actual file
        file = request.files['file']
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == "":
            return redirect(request.base_url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename = filename))
    else:
        return render_template('upload_file.html')


@app.route('/uploadedfile/<filename>')
def uploaded_file( filename ):
    return redirect("/uploadfile")
#    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


