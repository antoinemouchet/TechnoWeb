""" Module for diverse operations """

def find_user(existing_users, user):
    """
    Returns True if user is found in list of existing users

    Parameters
    ----------
    existing_users: list of already existing users (list)
    user: user to look for

    Returns
    -------
    True if user is in the list, false otherwise

    Note
    ----
    This function suppose that user is comparable to the elements of existing_users.
    """
    for existing in existing_users:
        if existing == user:
            return True
    
    return False


def add_user(data, username, first_name, surname, dob, password, group="normal", status=True, tasks=[]):
    """
    Adds an user in data with given parameters

    Parameters
    ----------
    data: the dict containing all the data with the users (dict at this point)
    username (str)
    first_name (str)
    surname (str)
    dob: date of birth (str)
    password (str)
    group: normal (default) or admin (str)
    status: true if account is accessible (default), false if blocked (bool)
    tasks : list of tasks of user (default = nothing in it) (list)

    Notes
    -----
    The group should only be normal or admin
    Tasks is a list of task (a task is a list with a specific format)
    --> A task follows the pattern [name, description, status, deadline]

    password is stored without any encrypting
    """
    data[username] = {"name": first_name,
                  "surname": surname,
                  "dob" : dob,
                  "password": password,
                  "group": group,
                  "status": status,
                  "tasks": tasks}


def create_task(task_name, deadline, description="", status=False):
    """
    Returns a task well constructed if no problem with it.

    Parameters
    ----------
    task_name: the name of the task (str)
    deadline: deadline of the task (str)
    description: description of the task (str)
    status: status (done/not done) of the task (bool)

    Returns
    -------
    False if there is a problem with any parameters,
    the task as [name, description, status, deadline] otherwise
    """
    # Validation of a task
    # 0: task_name, 1: description, 2:status, 3:deadline
    return [task_name, description, status, deadline]

def add_task(data, username, task):
    """
    Adds a task in data for an user

    Parameters
    ----------
    data: the dict containing all the data with the users (dict at this point)
    username (str)
    task: the task to add (list)

    Notes
    -----
    A task follows the pattern [name, description, status, deadline]
    """
    data[username]["tasks"].append(task)

def un_block_user(data, username, status):
    """
    Modifies status of an user's account

    Parameters
    ----------
    data: the dict containing all the data with the users (dict at this point)
    username (str)
    status: the new status (bool)

    Notes
    -----
    An admin account can not be blocked.
    A false status is equivalent to a blocked account
    """
    if data[username]["group"] != "admin":
        data[username]["status"] = status


def change_user_group(data, username, newGroup):
    """
    Changes the group of an user to match newGroup

    Parameters
    ----------
    data: the dict containing all the data with the users (dict at this point)
    username (str)
    newGroup: string representing the group of the user (str)

    Notes
    -----
    newGroup should be normal or admin ONLY
    """
    data[username]["group"] = newGroup