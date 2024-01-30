#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys
import csv


if __name__ == "__main__":
    _url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    
    user_res = requests.get(_url + "users/{}".format(user_id))

    user = user_res.json()

    username = user.get("username")

    params = {"userId": user_id}

    todos_res = requests.get(_url + "todos", params=params)

    todos = todos_res.json()

    with open("{}.csv".format(user_id), "w" , newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user_id, username, todo.get("completed"),
                             todo.get("title")])
