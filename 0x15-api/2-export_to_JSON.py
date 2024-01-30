#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
import json


if __name__ == "__main__":
    _url = "https://jsonplaceholder.typicode.com/"

    USER_ID = sys.argv[1]
    
    user = requests.get(_url + "users/{}".format(USER_ID)).json()

    username = user.get("username")

    params = {"userId": USER_ID}

    todos = requests.get(_url + "todos", params=params).json()

    export_data = {USER_ID: []}

    for todo in todos:
        task_inf = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
        }
        export_data[USER_ID].append(task_inf)

    with open("{}.json".format(USER_ID), "w") as jsonfile:
        json.dump(export_data, jsonfile, indent=4)
