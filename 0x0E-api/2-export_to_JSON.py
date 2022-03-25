#!/usr/bin/python3
"""
Pulls some 'employee' data from a fake api
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """the main code"""
    usersurl = "https://jsonplaceholder.typicode.com/users/"
    todosurl = "https://jsonplaceholder.typicode.com/todos/?userId="
    try:
        employeeid = int(argv[1])
    except (ValueError, TypeError):
        raise TypeError(
            "Employee ID must be an integer. Syntax: {} <employeeid>".format(
                argv[0]))
    # print(employeeid)
    requesturl = usersurl + str(employeeid)
    response = requests.get(requesturl)
    # print(response.json())
    reply = response.json()
    # print(reply["name"])
    name = reply.get("name")
    username = reply.get("username")
    requesturl = todosurl + str(employeeid)
    response = requests.get(requesturl)
    reply = response.json()
    task_list = []
    for item in reply:
        new_dict = {
            "task": item.get("title"),
            "completed": item.get("completed"),
            "username": username
            }
        task_list.append(new_dict)
    done_dict = {str(employeeid): task_list}
    out_file = open("{}.json".format(str(employeeid)), "w")
    json.dump(done_dict, out_file)
    out_file.close()
    # print("made dict: {}".format(done_dict))
    # print(reply)
    # print(len(reply))
    tasksqty = len(reply)
    requesturl = requesturl + "&completed=true"
    response = requests.get(requesturl)
    reply = response.json()
    completedtasksqty = len(reply)
    # print(len(reply))
    print("Employee {} is done with tasks({}/{}):".format(
        name, completedtasksqty, tasksqty
    ))
    for task in reply:
        # print("task title: {}".format(task["title"]))
        print("\t {}".format(task.get("title")))
