#!/usr/bin/python3
"""
extend a Python script to export data
"""
import json
import requests
from sys import argv


def export_json():
    """ function that saves data into a JSON file """
    url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        employee_name = content.get('username')
        employee_id = argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/' + \
            argv[1] + '/todos'

        response = requests.get(url)
        if response.status_code == 200:
            content = response.json()
            filename = argv[1] + '.json'
            tasks_list = []

            for task in content:
                list_ = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': employee_name}
                tasks_list.append(list_)

            with open(filename, 'w') as file:
                json_dict = json.dumps({'{}'.format(employee_id): tasks_list})
                file.write(json_dict)


if __name__ == "__main__":
    """ executing function """
    export_json()
