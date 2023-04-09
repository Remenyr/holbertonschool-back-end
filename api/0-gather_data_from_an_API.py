#!/usr/bin/python3
"""
This module containts an api request
"""
import requests
import sys


def gather_data_from_api():
    """
        This function gather data from an api
    """

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId='
    url_name = 'https://jsonplaceholder.typicode.com/users?id='
    response_todo = requests.get(url_todo + sys.argv[1])
    response_name = requests.get(url_name + sys.argv[1])

    content_todo = list(response_todo.json())
    content_name = list(response_name.json())

    task_completed = 0
    total_tasks = 0
    completed_tasks = []
    for elem in content_todo:
        if elem['completed']:
            task_completed += 1
            completed_tasks.append(elem['title'])
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        content_name[0]['name'], task_completed, total_tasks))
    for elem in completed_tasks:
        print('\t ' + elem)


if __name__ == "__main__":
    gather_data_from_api()
