#!/usr/bin/python3
"""
module to grab employees progress
on tasks in their todo list
"""

import csv
import requests
import sys


def get_employee_todo(employee_id):
    """
    get employee details
    Args:
        employee_id (_type_)
    """
    employee_url = f"https://jsonplaceholder.typicode.com" \
        f"/users/{employee_id}"
    response = requests.get(employee_url)

    if response.status_code != 200:
        print("Failed to fetch employee details")
        return

    employee_data = response.json()
    employee_name = employee_data['name']

    todos_url = f"https://jsonplaceholder.typicode.com/" \
        f"todos?userID={employee_id}"

    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Failed to fetch TODO list")
        return

    todos_data = response.json()
    
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name,
                             task['completed'], task['title']])

    print(f"Data exported to {csv_filename}")

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
