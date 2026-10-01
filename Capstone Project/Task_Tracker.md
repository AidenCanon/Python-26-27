# Reflection
I did end up using AI in assisting in naming the functions but i did come up with my own names but ended up deciding to go with the ones AI came up with they overall sounded better than mine and at the same time made it more understandable.
I used AI a second time i was actually having a problem where i could not get my stuff to output and it was just coming up blank in the terminal so i had the AI go through and check my grammar and if i made any mistakes which the reason it was having a problem was when i was calling the function i had something typed in wrong.

---

# Functions and What they do

* I started out with the add task function and this creates the stuff into a dictionaries for it to be called on.
* The get_positive_minutes function does exactly what it says makes sure any minutes added will be positive and cannot be below or be 0.
* The get valid_due_date is just checking your adding a valid date such as for example 10/1/2026 it will make sure you add it just like that but with dashes instead -.
* The total_minutes function is to calculate say you have two assignments and plan to spend 30 minutes on both it will add them up and display 60 total minutes so that you know how long in total you want to spend on all of the assignments int he task list.
* The display_tasks function when called on displays your tasks that are in the list.
* The user_input_task function is where the user input gets displayed from to receive the data and this is where the variable for minutes zeros out and the minutes function for positive minutes gets called along with that we ask what the status is whether it is still pending or completed.
* The main function is where the list of what you can do is displayed and this also where the tasks get inputted into via tasks = [] and it also uses if, elif, and else to get the choice and input of what number you choose.

---

# How to Use in terminal

- Run the python file.
- Once the file is running Choose 1, 2, or 3 and type this into terminal.
- If 1 is chosen 
    - Input course name and click enter
    - Next input assignment name and click enter
    - Next enter due date just like this but with your date in number MM-DD-YYYY
    - Finally enter your minutes and click enter
- If 2 is chosen it will display your tasks you have entered 
- If 3 is chosen it will exit and say Goodbye

---