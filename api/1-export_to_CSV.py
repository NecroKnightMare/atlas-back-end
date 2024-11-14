#!/usr/bin/python3
"""
module to grab employees progress
on tasks in their todo list
"""
import argparse
import csv
import requests
import sys


def get_employee_todo(employee_id):
    """
    get employee details
    Args:
        employee_id (_type_)
    """
    try:
        employee_url = f"https://jsonplaceholder.typicode.com" \
            f"/users/{employee_id}"
        response = requests.get(employee_url)

        if response.status_code != 200:
            raise ValueError(f"Failed to fetch employee details. Status code: {response.status_code}")

        employee_data = response.json()
        employee_name = employee_data['name']

        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        todos_response = requests.get(todos_url, timeout=10)

        if todos_response.status_code != 200:
            raise ValueError(f"Failed to fetch TODO list. Status code: {todos_response.status_code}")

        todos_data = todos_response.json()

        csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Employee ID", "Name", "Completed", "Task Title"])
            for task in todos_data:
                writer.writerow([employee_id, employee_name, task['completed'],
                task['title']])

        print(f"Data exported to {csv_filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {str(e)}")
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    
    return False

def main():
    parser = argparse.ArgumentParser(description='Export employee TODO list to CSV')
    parser.add_argument('employee_id', type=int, help='Employee ID')
    args = parser.parse_args()

    success = get_employee_todo(args.employee_id)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
