""" 
Task Tracker Application

This module provides functionality to track tasks, including adding, updating,
and deleting tasks. It also allows users to view tasks based on their status.

Goal is to get user input for tasks and manage them efficiently.
"""

import json
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("Task_Save_experimental.json")

5

def load_tasks(file_path):
    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["Task List"]

# Add a new task to the task list 
def add_task(task_list, course, assignment, due_date, total_minutes, status="Pending"):
    task = {
        "Course": course,
        "Assignment": assignment,
        "DueDate": due_date,
        "TotalMinutes": total_minutes,
        "Status": status
    }
    task_list.append(task)
    return task

#Validates whether the total minutes entered is positive
def get_positive_minutes(total_minutes):    
    return max(0, total_minutes)

#Validates whether the due date entered is in the correct format
def get_valid_due_date(due_date):
    from datetime import datetime
    try:
        valid_date = datetime.strptime(due_date, "%m-%d-%Y")
        return valid_date.strftime("%m-%d-%Y")
    except ValueError:
        return None
    
#Calculates the total minutes for all tasks in the task list
def total_minutes(task_list):
    return sum(task["TotalMinutes"] for task in task_list)

#Displays all tasks and the total minutes for all tasks
def display_tasks(task_list):
    if not task_list:
        print("No tasks have been added yet.")
    for task_number, task in enumerate(task_list, start=1):
        print(f"\n{task_number}. Course: {task['Course']}, Assignment: {task['Assignment']}, Due Date: {task['DueDate']}, Total Minutes: {task['TotalMinutes']}, Status: {task['Status']}")
    print(f"Total Minutes for all tasks: {total_minutes(task_list)}")

#Handles user input for adding a new task
def user_input_task(task_list):
    course = input("Enter course name: ")
    assignment = input("Enter assignment name: ")
    due_date = None
    while due_date is None:
        due_date = get_valid_due_date(input("Enter due date (MM-DD-YYYY): "))
        if due_date is None:
            print("Please enter a valid date in MM-DD-YYYY format.")

    minutes = 0
    while minutes <= 0:
        try:
            minutes = get_positive_minutes(int(input("Enter total minutes required: ")))
            if minutes <= 0:
                print("Minutes must be greater than zero.")
        except ValueError:
            print("Please enter a whole number of minutes.")

    status = input("Enter status (Pending/Completed): ").strip().title() or "Pending"
    return add_task(task_list, course, assignment, due_date, minutes, status)

#Main function to run the task tracker application
def main():
    tasks = load_tasks(TASKS_FILE)
    while True:
        print("\nTask Tracker")
        print("1. Add task")
        print("2. Edit task")
        print("3. List tasks")
        print("4. Exit")
        print("5. Remove task")
        print("6. Save tasks and exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            user_input_task(tasks)
            save_tasks(tasks, TASKS_FILE)
            print("Task added.")
        elif choice == "2":
            display_tasks(tasks)
            try:
                task_number = int(input("Enter the number of the task to edit: "))
                if 1 <= task_number <= len(tasks):
                    task_index = task_number - 1
                    course = input("Enter new course name (leave blank to keep current): ").strip() or None
                    assignment = input("Enter new assignment name (leave blank to keep current): ").strip() or None
                    due_date = get_valid_due_date(input("Enter new due date (MM-DD-YYYY) (leave blank to keep current): ").strip()) or None
                    minutes = input("Enter new total minutes required (leave blank to keep current): ").strip()
                    minutes = int(minutes) if minutes else None
                    status = input("Enter new status (Pending/Completed) (leave blank to keep current): ").strip().title() or None
                    edit_task(tasks, task_index, course, assignment, due_date, minutes, status)
                    save_tasks(tasks, TASKS_FILE)
                    print("Task updated.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            print("Goodbye.")
            break
        elif choice == "5":
            display_tasks(tasks)
            if not tasks:
                print("There are no tasks to remove.")
                continue
            try:
                task_number = int(input("Enter the number of the task to remove: "))
                if remove_task(tasks, task_number - 1):
                    save_tasks(tasks, TASKS_FILE)
                    print("Task removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == "6":
            save_tasks(tasks, TASKS_FILE)
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, 3, 4, 5, or 6.")

#Experimental Functions for testing and development purposes
def save_tasks(task_list, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump({"Task List": task_list}, file, indent=4)
    print(f"Tasks saved to {file_path}.")

#Removes a task by its zero-based index
def remove_task(task_list, task_index):
    if 0 <= task_index < len(task_list):
        del task_list[task_index]
        return True
    return False

def edit_task(task_list, task_index, course=None, assignment=None, due_date=None, minutes=None, status=None):
    if 0 <= task_index < len(task_list):
        if course is not None:
            task_list[task_index]["Course"] = course
        if assignment is not None:
            task_list[task_index]["Assignment"] = assignment
        if due_date is not None:
            task_list[task_index]["DueDate"] = due_date
        if minutes is not None:
            task_list[task_index]["TotalMinutes"] = minutes
        if status is not None:
            task_list[task_index]["Status"] = status
        return True
    return False

#Entry point for the application
if __name__ == "__main__":
    main()
