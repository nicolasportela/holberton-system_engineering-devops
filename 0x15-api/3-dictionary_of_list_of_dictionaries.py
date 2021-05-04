#!/usr/bin/python3
"""Python script to export data from ALL employees in the JSON format"""

if __name__ == "__main__":
    import json
    import requests

    r = requests.get("https://jsonplaceholder.typicode.com/users").json()
    r2 = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    bigdict = {}
    userdict = {}

    for users in r:
        id = users.get("id")
        bigdict[id] = []
        userdict[id] = users.get("username")

    for tasks in r2:
        tasksdict = {}
        id = tasks.get("userId")
        tasksdict["task"] = tasks.get('title')
        tasksdict["completed"] = tasks.get('completed')
        tasksdict["username"] = userdict.get(id)
        bigdict.get(id).append(tasksdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(bigdict, jsonfile)
