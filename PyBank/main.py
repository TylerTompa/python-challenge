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

# The variable changes is a list which stores the change in profits for each month.  The suceeding for-loop will find the difference between each pair of adjancent months and store them in this list.  We will then be able to use primitive functions to find the sum and length of this list, and thereafter the average.
changes = []
for i in range(len(profits)):
    if i not in (0,1):
        change = int(profits[i]) - int(profits[i-1])
        changes.append(change)

max_change = max(changes)
print(max_change)
max_change_index = changes.index(max(changes))
print(max_change_index)
offset = max_change_index + 2
print(months[offset])

print("Financial Analysis")
print("----------------------------")
print(f"Total months: {len(months)-1}")
print(f"Total profits: {total_profit}")
print(f"Average Change: {(sum(changes)/len(changes)):.2f}")
print(f"Greatest Increase in Profits: {months[offset]} (${max(changes)})")
print(f"Greatest Decreast in Profits: (${min(changes)})")