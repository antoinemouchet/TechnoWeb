import os, binascii

class Config(object):
    SECRET_KEY = binascii.hexlify(os.urandom(24))


# Global variable because it's needed by more than one file

global users


users = {"admin": {"name": "admin",
                  "surname": "admin",
                  "dob" : "21-10-2020",
                  "password": "secret",
                  "group": "admin",
                  "status": True,
                  # a task follows the pattern [name, description, status, deadline]
                  "tasks": []
                    }
        }
