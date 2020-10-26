""" Module for diverse operations """

def check_task_in(taskList, taskID):
    """
    Returns true if task is in the list of task, false otherwise

    Parameters
    ----------
    taskList: list of task Objectcs (list)\n
    taskID: id of task we check (int)

    Returns
    -------
    True if task is in the list
    """
    for t in taskList:
        if t.id == taskID:
            return True

    return False

def check_user_in(userList, username):
    """
    Returns true if the user is in the list of users, false otherwise

    Parameters
    ----------
    userList: list of users Objectcs (list)\n
    username: username we check (str)

    Returns
    -------
    True if user is in the list
    """
    for u in userList:
        if u.username == username:
            return True

    return False





        