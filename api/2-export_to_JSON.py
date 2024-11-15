#!/usr/bin/python3
"""
For a given employee ID, returns information about
task progress and exports data in JSON format.
"""

import json
import requests
import sys


def fetch_user(employee_id):
    """Fetch user information by ID"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()  # error for bad status codes
    return response.json()


def fetch_todos(employee_id):
    """Fetch todos for a specific user ID
    params will be used as variable as well"""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={'userId': employee_id})
    response.raise_for_status()  # error for bad status codes
    return response.json()


def export_to_json(data, filename):
    """Export data to a JSON file"""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def main(employee_id):
    user_data = fetch_user(employee_id)
    employee_name = user_data.get('name')

    todos_data = fetch_todos(employee_id)

    tasks_list = [
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee_name
        }
        for todo in todos_data
    ]

    export_to_json({employee_id: tasks_list}, f"{employee_id}.json")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID should be an integer.")
        sys.exit(1)

    main(employee_id)
