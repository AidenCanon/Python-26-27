# Week 7 - Capstone Proposal 

## Project Name

Task Tracker Application 

---

## Project Purpose

Create a Python console app that helps College student track there course name and assignment.

---

## Main Features

* Add a course name
* add a task
* list current tasks
* Show the time they plan to spend on that assignment 
* Show Assignment deadline
* Total amount of time added up from each assignment 

---

### Potential/Backlog Features

- delete a task
- edit a task
- Saving the tasks

  
---

## Inputs

* course name
* task name
* estimated minutes
* Due Date

---

## Outputs

* readable task list
* total planned minutes

---

## Likely Structure

* list of dictionaries for task data
* functions for add, display, complete, and summarize
* Possible Functions:
    * add_task(tasks) — ask for course, assignment name, estimated minutes, and due date, then add a task.
    * display_tasks(tasks) — show each task in a readable format.
    * get_positive_minutes(prompt) — ensure estimated time is a positive number.
    * get_valid_due_date(prompt) — accept only dates in the format you choose.
    * total_planned_minutes(tasks) — add up the estimated time.
I did have my own but i liked how the AI Presented these functions.
---

## Risks

* adding deadlines, files, editing, deleting, and saving may make the project too large
* task deletion and editing could increase complexity if added too early

---

## AI Use Plan

AI may be used to:

* compare function organization
* suggest validation checks
* review output wording

AI will not choose:

* project purpose
* final scope
* whether the code is correct without testing