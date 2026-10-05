""" 
Task Tracker Application

This module provides functionality to track tasks, including adding, updating,
and deleting tasks. It also allows users to view tasks based on their status.

Goal is to get user input for tasks and manage them efficiently.
"""
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
    for task in task_list:
        print(f"\nCourse: {task['Course']}, Assignment: {task['Assignment']}, Due Date: {task['DueDate']}, Total Minutes: {task['TotalMinutes']}, Status: {task['Status']}")
    print(f"\nTotal Minutes for all tasks: {total_minutes(task_list)}")

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
    tasks = []
    while True:
        print("\nTask Tracker")
        print("1. Add task")
        print("2. List tasks")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            user_input_task(tasks)
            print("Task added.")
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Choose 1, 2, or 3.")

#Entry point for the application
if __name__ == "__main__":
    main()

