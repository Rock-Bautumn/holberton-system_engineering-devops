#!/usr/bin/python3
"""
Pulls some 'employee' data from a fake api
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """the main code"""
    usersurl = "https://jsonplaceholder.typicode.com/users"
    todosurl = "https://jsonplaceholder.typicode.com/todos"
    # print(employeeid)
    response = requests.get(usersurl)
    # print(response.json())
    reply = response.json()
    user_dict = {}
    for item in reply:
        user_dict[item.get("id")] = item.get("username")

    # print(str(user_dict))
    # { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    done_dict = {}
    for user in user_dict.keys():
        done_dict[str(user)] = []
    # print(done_dict)
    response = requests.get(todosurl)
    reply = response.json()
    # print(f"we got {reply}")
    for item in reply:
        # print(f"------------------------------------------------------")
        # print("todo id is : {}".format(str(item.get("id"))))
        new_dict = {
            "username": user_dict.get(item.get("userId")),
            "task": item.get("title"),
            "completed": item.get("completed"),
            }
        empId = str(item.get("userId"))
        # print(f"empId: {empId}")
        # print(f"new_dict: {new_dict}")
        # print(type(done))
        # print("done dict is: {}".format(done_dict))
        # print("done dict empId: {}".format(done_dict.get(empId)))
        if done_dict[empId] == []:
            done_dict[empId] = [new_dict]
        else:
            ml = list(done_dict.get(empId))
            # print(f"ml is {ml} type {type(ml)}")
            if type(ml) == list:
                done_dict[empId].append(new_dict)
        # print(f"done dict at the end of todo id {str(item.get('id'))} is {done_dict}")
    out_file = open("todo_all_employees.json", "w")
    json.dump(done_dict, out_file)

    out_file.close()
