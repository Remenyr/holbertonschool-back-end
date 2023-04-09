#!/usr/bin/python3
"""
Python script that, using a REST API, returns
info about an employee todo list
"""

import requests
from sys import argv


if __name__ == "__main__":
    """
    For a given employee ID, returns information about
    his/her todo list progress.
    """
    url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        content = response.json()
        employee_name = content.get('name')
        url = 'https://jsonplaceholder.typicode.com/users/' + \
            argv[1] + '/todos'

        response = requests.get(url)
        if response.status_code == 200:
            content = response.json()
            number_done_tasks = 0
            tasks_title = []

            for dic in content:
                if dic['completed'] is True:
                    number_done_tasks += 1
                    tasks_title.append(dic['title'])

            print("Employee {} is done with tasks({}/{}):".format(
                employee_name,
                number_done_tasks,
                len(content)))
            [print("\t {}".format(title)) for title in tasks_title]
