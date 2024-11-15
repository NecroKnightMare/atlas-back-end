#!/usr/bin/python3
"""
module to grab employees progress
on tasks in their todo list
"""

import requests
import sys
# def get_employee_progress(employee_id):
#     """
#     get employee details
#     Args:
#         employee_id (int)
#     """
#     user_data = user_response.json()
#     employee_name = user_data.get('name')

#     base_url = f"https://jsonplaceholder.typicode.com"

#     if not isinstance(employee_id, int):
#         raise TypeError("employee_id must be an integer.")

#     employee_url = f"{base_url}/users/{employee_id}"
#     employee_response = requests.get(employee_url).json()

#     if employee_response.status_code == 200:
#         employee_data = employee_response.json()
#     else:
#         print(f"Invalid emlpoyee id")
#         return

#     todo_url = f"{base_url}/todos?userId={employee_id}"
#     todo_response = requests.get(todo_url).json()

#     if todo_response.status_code == 200:
#         todo_data = todo_response.json()
#     else:
#         print(f"No todo list found")
#         return

#     employee_name = employee_response.get("username")
#     total_tasks = len(todo_data)
#     completed_tasks = [task.get("title")
#                        for task in todo_data if task.get("completed")]

#     print(f"Employee {employee_name} is done with tasks"
#           f"({len(completed_tasks)}/{total_tasks}):")
#     for task in completed_tasks:
#         print(f"\t {task}")

#     user_response = requests.get("{}/users/{}".format(base_url, employee_id))
#     if user_response.status_code != 200:
#         print("Error fetching user with ID {}".format(employee_id))
#         return
#     # user_data = user_response.json()
#     # employee_name = user_data.get('name')

#     todos_response = requests.get("{}/todos?userId={}"
#                                   .format(base_url, employee_id))
#     if todos_response.status_code != 200:
#         print("Error fetching TODO list for user with ID {}"
#               .format(employee_id))

#     todos_data = todos_response.json()

#     total_tasks = len(todos_data)
#     done_tasks = [task for task in todos_data if task.get('completed')]
#     number_of_done_tasks = len(done_tasks)

#     print(f"Employee {employee_name} is done with tasks"
#           f"({len(completed_tasks)}/{total_tasks}):")

#     for task in done_tasks:
#         print(f"\t {task.get('title')}")

#     if __name__ == "__main__":
#         if len(sys.argv) != 2:
#             print("Usage: employee id")
#             sys.exit(1)
#         else:
#             try:
#                 employee_id = int(sys.argv[1])
#             except ValueError:
#                 print("Provide correct employee name")
#                 sys.exit(1)

#      get_employee_progress(int(sys.argv[1])


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
