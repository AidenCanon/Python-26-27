""" 
Assignment 8
The goal is to complete the assignment and to have it read the file contents correctly.
"""

# Import the Path class from the pathlib module to handle file paths
from pathlib import Path

# Define the path to the input file
input_file = Path(__file__).with_name("assignment_8_file.txt")

# Define the path to the output file
output_file = Path(__file__).with_name("assignment_8_file_2.txt")

# Define the list of games to be written to the output file
games = [
    "Game Tracker",
    "------------",
    "1. Apex Legends",
    "2. Fortnite",
    "3. Valorant"
]

# Write the list of games to the output file
with output_file.open("w", encoding="utf-8") as file:
    file.write("\n".join(games))

# Open the output file and read its contents
with output_file.open("r", encoding="utf-8") as file:
    contents2 = file.read()

# Print a message indicating that the file has been written to
print("Wrote to File: ", output_file.name)

# Print the loaded file name and its contents for the second file
print("Loaded From File: ", output_file.name)
print("Contents: ", contents2)




# Open the input file and read its contents
with input_file.open("r", encoding="utf-8") as file:
    contents = file.read()

# Print the loaded file name and its contents
print("Loaded From File: ", input_file.name)
print("Contents: ", contents)

