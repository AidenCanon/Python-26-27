"""
Assignment 7
The task here is for me to create a task tracker. The goal is to use a class, Attribute, and methods to manage tasks efficiently.
"""
# Task Tracker Class Implementation
class TaskTracker:
    def __init__(self):
        # This is an attribute to store all tasks in the tracker
        self.tasks = []
# Method to add a task to the tracker
    def add_task(self, task):
        self.tasks.append(task)
# Method to display all tasks in the tracker
    def show_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            print("-", task)
            

# Creating an instance of the TaskTracker class and adding tasks to it
Task = TaskTracker()
Task.add_task("Complete Assignment 7")
Task.add_task("Review notes for Week 4")
Task.add_task("Prepare for week 5")
Task.show_tasks()
    