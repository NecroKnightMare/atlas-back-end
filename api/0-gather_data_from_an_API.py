 #!/usr/bin/python3
"""
"""

import requests
import sys


def get_employee_todo(employee_id):
    """

    Args:
        employee_id (_type_): _description_
    """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)

    if response.status_code != 200:
        print("Failed to fetch employee details")
        return

    employee_data = response.json()
    employee_name = employee_data['name']

    todos_url = f"https://jsonplaceholder.typicode.com/todos?userID={employee_id}"
    
    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Failed to fetch TODO list")
        return

    todos_data = response.json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python3 script.py <employee_id>")
            sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
            get_employee_todo(employee_id)
        except ValueError:
            print("Employee id must be an integer")
            sys.exit(1)
