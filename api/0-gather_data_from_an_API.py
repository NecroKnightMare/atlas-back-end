#!/usr/bin/python3
"""
module to grab employees progress
on tasks in their todo list
"""

import requests
import sys

base_url = f"https://jsonplaceholder.typicode.com"


def get_employee_progress(employee_id):
    """
    get employee details
    Args:
        employee_id (int)
    """
    if not isinstance(employee_id, int):
        raise TypeError("employee_id must be an integer.")

    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url).json()

    if employee_response.status_code == 200:
        employee_data = employee_response.json()
    else:
        print(f"Invalid emlpoyee id")
        return

    todo_url = f"{base_url}/todos?userId={employee_id}"
    todo_response = requests.get(todo_url).json()

    if todo_response.status_code == 200:
        todo_data = todo_response.json()
    else:
        print(f"No todo list found")
        return

    employee_name = employee_response.get("username")
    total_tasks = len(todo_data)
    completed_tasks = [task.get("title")
                       for task in todo_data if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: employee id")
            sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
        except ValueError:
            print("Provide correct employee name")
            sys.exit(1)

        get_employee_progress(int(sys.argv[1]))
