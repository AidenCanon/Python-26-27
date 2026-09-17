""" 
Assignment 10
The goal for this assignment is to create 2 different data representations.
"""
# Class to represent a Brewers win with date, runs, and win status
class BrewersWin:
    def __init__(self, date, runs, win):
        self.date = date
        self.runs = runs
        self.win = win
# Plain text representation of a Brewers win
plain_text_Style ="September 11, 2026 | 20 runs | Win"

# Object-oriented representation of a Brewers win
Object_Style = BrewersWin("September 11, 2026", 20, True)

# Display both representations of a Brewers win
print("Plain Text Style:")
print(plain_text_Style)

# Display the object-oriented representation of a Brewers win
print("\nObject Style:")
print(f"{Object_Style.date} | {Object_Style.runs} runs | {'Win' if Object_Style.win else 'Loss'}")