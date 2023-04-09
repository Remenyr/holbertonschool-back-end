#!/usr/bin/python3
"""
extend your Python script to export data
"""
import requests
from sys import argv


def export_csv():
    """ function that saves data into a csv file """
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
            filename = argv[1] + '.csv'
            print(employee_name, employee_id)

            with open(filename, 'w') as file:
                for dic in content:
                    file.write('"{}","{}","{}","{}"\n'.format(
                        employee_id, employee_name,
                        dic['completed'], dic['title']))


if __name__ == "__main__":
    """ executing function """
    export_csv()
