#!/usr/bin/python3
"""
This module containts an api request
"""
import json
import requests


def gather_data_from_api():
    """
        This function gather data from an api
    """

    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    response_todo = requests.get(url_todo)
    response_users = requests.get(url_users)

    content_todo = list(response_todo.json())
    content_users = list(response_users.json())

    result = {}
    for user in content_users:

        attributes = []
        for elem in content_todo:
            aux_dict = {}
            aux_dict['username'] = user['username']
            aux_dict['task'] = elem['title']
            aux_dict['completed'] = elem['completed']

            if user['id'] == elem['userId']:
                attributes.append(aux_dict)

        result[user['id']] = attributes

    jsonString = json.dumps(result)
    with open('todo_all_employees.json', 'w') as f:
        f.write(jsonString)


if __name__ == "__main__":
    gather_data_from_api()
