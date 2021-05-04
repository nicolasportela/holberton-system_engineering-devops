#!/usr/bin/python3
"""script that for a given employee ID, returns his/her TODO list progress"""

if __name__ == "__main__":
    import csv
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

    with open("{}.csv".format(number), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in r2:
            taskwriter.writerow([number, username, task.get('completed'),
                                 task.get('title')])
