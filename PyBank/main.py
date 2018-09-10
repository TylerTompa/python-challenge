# The os package allows us to create custom file paths, and the csv package allows us to read csv files.
import os
import csv

csv_budget_data = os.path.join("Resources", "budget_data.csv")

with open(csv_budget_data, newline="") as csv_file:
    
    budget_data_reader = csv.reader(csv_file, delimiter=",")
    budget_data_header = next(budget_data_reader)
    print(budget_data_header)

    for row in budget_data_reader:
        print(row)
