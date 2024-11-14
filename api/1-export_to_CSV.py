#!/usr/bin/python3
"""
This module exports data to a CSV file.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports the task list of an employee to a CSV file
    """
    # Validate that employee_id is an integer
    if not isinstance(employee_id, int):
        raise TypeError("employee_id must be an integer.")

    # Define URLs for data retrieval
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    # Retrieve user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch User Data for Employee ID: {employee_id}")
        return
    user_data = user_response.json()

    # Retrieve to-do list data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch To-Do List for Employee ID: {employee_id}")
        return
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get("username")

    # Define CSV file name
    csv_filename = f"{employee_id}.csv"

    # Write to CSV file
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["Username", "Task", "Completed"])
        for task in todos_data:
            writer.writerow([employee_name, task.get("title"), task.get("completed")])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    try:
        export_to_csv(int(sys.argv[1]))
    except ValueError:
        print("Please provide a valid employee ID.")
