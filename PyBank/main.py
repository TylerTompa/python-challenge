# The os package allows us to create custom file paths, and the csv package allows us to read csv files.
import os
import csv

profit_losses_list = []

csv_budget_data = os.path.join("Resources", "budget_data.csv")

with open(csv_budget_data, newline="") as csv_file:
    
    budget_data_reader = csv.reader(csv_file, delimiter=",")
    budget_data_header = next(budget_data_reader)
    # print(budget_data_header)   

    # This iterates through the budget_data_reader variable to create a list, and thereafter computes the length of said list.
    total_months = len(list(budget_data_reader))

print(f"Total months: {total_months}")