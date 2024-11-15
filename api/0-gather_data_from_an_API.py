#!/usr/bin/python3
"""
module to grab employees progress
on tasks in their todo list
"""
import requests
import sys


def get_user_by_id(employee_id):
    """
    gets emplyee id
    """
    users_url = 'https://jsonplaceholder.typicode.com/users'
    try:
        users = requests.get(users_url).json()
        for user in users:
            if user['id'] == employee_id:
                return user['name']
    except requests.RequestException as e:
        print(f"Failed to fetch user data: {e}")
        return None
    return None


def get_todos_by_user(employee_id):
    """
    grabs todo data by employee
    """
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos = []
    try:
        all_todo = requests.get(todos_url).json()
        for todo in all_todos:
            if todos['userId'] == employee_id:
                todo.append(todos)
    except requests.RequestException as e:
        print(f"Failed to fetch todo data: {e}")
    return todos


def display_employee_progress(employee_name, todo):
    """
    Displays employee's
    TODO progress
    """
    completed_tasks = [todo["title"] for todo in todos if
          todo["completed"]]
    total_tasks = len(todos)
    print(f"Employee {employee_name} is done with"
          f"tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: employee id")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Provide a valid employee ID")
        sys.exit(1)

    employee_name = get_user_by_id(employee_id)
    if not employee_name:
        print("Employee ID not found")
        sys.exit(1)

    todos = get_todos_by_user(employee_id)
    if not todos:
        print("No tasks found")
        sys.exit(1)

    display_employee_progress(employee_name, todos)
