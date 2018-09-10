# The os package allows us to create custom file paths, and the csv package allows us to read csv files.
import os
import csv
import pandas

csv_budget_data = os.path.join("Resources", "budget_data.csv")

with open(csv_budget_data, newline="") as csv_file:
    
    # budget_data_reader = csv.reader(csv_file, delimiter=",")
    # budget_data_header = next(budget_data_reader)
    # # print(budget_data_header)   

    # The pandas package allows us to create lists which are composed of individual rows from a csv file.  
    column_names = ["date", "profits"]
    finances = pandas.read_csv(csv_budget_data, names=column_names)
    profits = finances.profits.tolist()
    months = finances.date.tolist()

total_profit = 0
for i in range(len(profits)):
    if i != 0:
        total_profit += int(profits[i])


print("Financial Analysis")
print("----------------------------")
print(f"Total months: {len(months)-1}")
print(f"Total profits: {total_profit}")
