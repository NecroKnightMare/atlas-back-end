#!/usr/bin/env python3
"""
module to grab employees progress
on tasks in their todo list
"""

import requests
import sys


def get_employee_progress(employee_id):
    """
    get employee details
    Args:
        employee_id (_type_)
    """
    if not isinstance(employee_id, int):
        raise TypeError("employee_id must be an integer.")

    user_url = f"https://jsonplaceholder.typicode.com" \
        f"/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com" \
        f"/todos?userId={employee_id}"

    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"Error: {employee_id}")
        return
    user_data = user_response.json()

    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"Error: todo {employee_id}")
        return
    todo_data = todo_response.json()

    employee_name = user_data.get("username")
    total_tasks = len(todo_data)
    completed_tasks = [task.get("title")
                       for task in todo_data if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

    if __name__ == "__main__":
        get_employee_progress(int(sys.argv[1]))
