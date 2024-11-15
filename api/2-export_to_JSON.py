#!/usr/bin/python3
"""
For a given employee ID, returns information about
task progress and exports data in JSON format.
"""

import json
import requests
import sys


# def fetch_user(employee_id):
#     """Fetch user information by ID"""
#     url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
#     response = requests.get(url)
#     response.raise_for_status()  # error for bad status codes
#     return response.json()


# def fetch_todos(employee_id):
#     """Fetch todos for a specific user ID
#     params will be used as variable as well"""
#     url = "https://jsonplaceholder.typicode.com/todos"
#     response = requests.get(url, params={'userId': employee_id})
#     response.raise_for_status()  # error for bad status codes
#     return response.json()


# def export_to_json(data, filename):
#     """Export data to a JSON file
#     """
#     with open(filename, 'w') as json_file:
#         json.dump(data, json_file)


# def main(employee_id):
#     user_data = fetch_user(employee_id)
#     employee_name = user_data.get('name')

#     todos_data = fetch_todos(employee_id)

#     tasks_list = [
#         {
#             "task": todo["title"],
#             "completed": todo["completed"],
#             "username": employee_name
#         }
#         for todo in todos_data
#     ]

#     export_to_json({employee_id: tasks_list}, f"{employee_id}.json")


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
#         sys.exit(1)

#     try:
#         employee_id = int(sys.argv[1])
#     except ValueError:
#         print("The employee ID should be an integer.")
#         sys.exit(1)

#     main(employee_id)
#!/usr/bin/python3
"""This module defines a script that connects to an API to fetch and export todo list progress"""


def fetch_employee_data(employee_id):
    """Fetch employee data by ID"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_todo_data(employee_id):
    """Fetch todo data for a specific employee ID"""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={'userId': employee_id})
    response.raise_for_status()
    return response.json()


def export_to_json(data, filename):
    """Export data to a JSON file"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def display_and_export_todo_progress(employee_id):
    """Display the todo list progress and export to JSON for a given employee ID"""
    employee_data = fetch_employee_data(employee_id)
    employee_name = employee_data.get('name')
    username = employee_data.get('username')

    todos = fetch_todo_data(employee_id)
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with"
          f" tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

    data = {
        str(employee_id): [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": username
            }
            for todo in todos
        ]
    }

    filename = f"{employee_id}.json"
    export_to_json(data, filename)
    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID should be an integer.")
        sys.exit(1)

    display_and_export_todo_progress(employee_id)
