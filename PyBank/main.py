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

# The variable changes is a list which stores the change in profits for each month.  The suceeding for loop will find the difference between each pair of adjancent months and store them in this list.
changes = []
change = 0
for i in range(len(profits)):
    if i != 0 and i != 1:
        change = (int(profits[i]) - int(profits[i-1])) / 2
        changes.append(change)

# for i in range(len(changes)):
#     print(changes[i])

# print("----------------------------")

# print(profits[2])
# print(profits[1])
# print(int(profits[2])-int(profits[1]))
# print(float(profits[2])-float(profits[1]))

the_sum = sum(changes)
the_len = len(changes)
the_avg = the_sum/the_len
print(the_avg)

print("Financial Analysis")
print("----------------------------")
print(f"Total months: {len(months)-1}")
print(f"Total profits: {total_profit}")
print(f"Average Change: {sum(changes)/len(changes)}")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decreast in Profits: ")