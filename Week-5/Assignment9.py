""" 
This file contains the Python code for Assignment 9 of Week 5.
"""
import csv
from pathlib import Path

input_file = Path(__file__).with_name("Assignment9.csv")

with input_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        price = int(row["price"])
        expensive = price > 0

        if row["expensive"].lower() == "true":
            expensive = True
        else:
            expensive = False
        
        print(row["games"], "-", row["platform"], "-", price,"$", "-", expensive)