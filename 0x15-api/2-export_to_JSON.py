#!/usr/bin/python3
"""Script to export data in the JSON format according to requirements"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    number = sys.argv[1]
    identityusers = {'id': number}
    r = requests.get("https://jsonplaceholder.typicode.com/users",
                     params=identityusers).json()
    username = r[0].get("username")
    identitytodos = {'userId': number}
    r2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                      params=identitytodos).json()

    tasks = []
    for task in r2:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[number] = tasks
    with open("{}.json".format(number), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
