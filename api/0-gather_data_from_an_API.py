#!/usr/bin/python3
"""
module to grab employees progress
on tasks in their todo list
"""
import requests
import sys


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


def display_todo_progress(employee_id):
    """Display the todo list progress for a given employee ID"""
    employee_data = fetch_employee_data(employee_id)
    employee_name = employee_data.get('name')

    todos = fetch_todo_data(employee_id)
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done"
          f"with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: employee")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID should be an integer.")
        sys.exit(1)

    display_todo_progress(employee_id)
