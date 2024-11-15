#!/usr/bin/python3
"""
Export all employee tasks in JSON format
"""
import json
import requests


def fetch_users():
    """Fetch all users"""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()  # error for bad status codes
    return response.json()


def fetch_todos():
    """Fetch all todos"""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    response.raise_for_status()  # error for bad status codes
    return response.json()


def export_to_json(data, filename):
    """Export data to a JSON file"""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def main():
    users = fetch_users()
    todos = fetch_todos()

    all_data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos if todo["userId"] == user_id
        ]
        all_data[user_id] = user_tasks

    export_to_json(all_data, "todo_all_employees.json")


if __name__ == "__main__":
    main()
