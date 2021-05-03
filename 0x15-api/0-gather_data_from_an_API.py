#!/usr/bin/python3
"""script that for a given employee ID, returns his/her TODO list progress"""

if __name__ == "__main__":
    import requests
    import sys

    number = sys.argv[1]
    identityusers = {'id': number}
    r = requests.get("https://jsonplaceholder.typicode.com/users",
                     params=identityusers).json()
    name = r[0].get("name")
    identitytodos = {'userId': number}
    r2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                      params=identitytodos).json()
    done = 0
    donelist = []
    total = len(r2)
    for dict in r2:
        if dict.get("completed") is True:
            done = done + 1
            donelist.append(dict.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for j in range(len(donelist)):
        print("\t {}".format(donelist[j]))
