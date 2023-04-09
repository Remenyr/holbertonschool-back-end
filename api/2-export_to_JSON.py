#!/usr/bin/python3
"""
This module containts an api request
"""
import json
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

    attributes = []
    for elem in content_todo:
        aux_dict = {}
        aux_dict['task'] = elem['title']
        aux_dict['completed'] = elem['completed']
        aux_dict['username'] = content_name[0]['username']
        attributes.append(aux_dict)

    result = {}
    result['{}'.format(sys.argv[1])] = attributes

    jsonString = json.dumps(result)

    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        f.write(jsonString)


if __name__ == "__main__":
    gather_data_from_api()
