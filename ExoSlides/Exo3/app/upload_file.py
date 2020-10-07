import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

"""
This function makes sure the file is a file with an allowed extension.

Parameters
----------
file_name: path of file (str)

Returns
-------
True if file as allowed_extension
"""
def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS