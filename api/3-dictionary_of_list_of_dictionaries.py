#!/usr/bin/python3
"""
extend a Python script to export data
"""
import json
import requests


def export_all_json():
    """ function that saves all data into a JSON file """
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        dic_user = {}
        filename = 'todo_all_employees.json'

        for user in content:
            employee_usernmane = user.get('username')
            employee_id = user.get('id')
            url = 'https://jsonplaceholder.typicode.com/users/' + \
                str(employee_id) + '/todos'
            response = requests.get(url)

            if response.status_code == 200:
                content = response.json()
                tasks_list = []

                for task in content:
                    list_ = {
                        'username': employee_usernmane,
                        'task': task['title'],
                        'completed': task['completed']}
                    tasks_list.append(list_)
                    dic_user[employee_id] = tasks_list

        with open(filename, 'w') as file:
            json_dict = json.dumps(dic_user)
            file.write(json_dict)


if __name__ == "__main__":
    """ executing function """
    export_all_json()
