import os, binascii
class Config(object): # path of the folder where the file is to be uploaded to the server
    UPLOAD_FOLDER = "/home/users/100/amouchet/Documents/TechnoWeb/ExoSlides/Exo3/app/static/uploads/"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    # 16 Megabyte
    SECRET_KEY = binascii.hexlify(os.urandom(24))
    #  os.urandom(size)  generates  a  string  (size  bytes)  containing  random characters.
    # binascii.hexlify Return  the  hexadecimal  representation  of  the binary data