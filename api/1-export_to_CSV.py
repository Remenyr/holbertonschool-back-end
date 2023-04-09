#!/usr/bin/python3
"""
This module containts an api request
"""
import csv
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

    result = []
    for elem in content_todo:
        aux_list = []
        aux_list.append(str(elem['userId']))
        aux_list.append(str(content_name[0]['username']))
        aux_list.append(str(elem['completed']))
        aux_list.append(str(elem['title']))
        result.append(aux_list)

    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        write.writerows(result)


if __name__ == "__main__":
    gather_data_from_api()
