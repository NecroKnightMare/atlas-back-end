#!/usr/bin/python3
"""
module to grab employees progress
on tasks in their todo list
"""

import requests
import sys


def get_employee_data(employee_id):
    """
    get employee details
    Args:
        employee_id (_type_)
    """
    user_url = f"https://jsonplaceholder.typicode.com" \
        f"/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com" \
        f"/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200 or todo_response:
        print("Error: Unable to fetch employee details")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    return user_data, todo_data


def show_progress(employee_id):
    user_data, todo_data = get_employee_data(employee_id)

    employee_name = user_data.get("username")
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]
    done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
            sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
            get_employee_data(employee_id)
        except ValueError:
            print("Error: Employee id must be an integer")
            sys.exit(1)
