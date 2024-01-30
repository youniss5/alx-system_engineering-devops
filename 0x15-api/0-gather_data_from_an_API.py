#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    _url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user_res = requests.get(_url + "users/{}".format(employee_id))

    user = user_res.json()

    params = {"userId": employee_id}

    todos_res = requests.get(_url + "todos", params=params)

    todos = todos_res.json()

    completed = []
    
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(user.get("name"),
                                                         len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
