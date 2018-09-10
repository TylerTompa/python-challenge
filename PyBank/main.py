# The os package allows us to create custom file paths, and the pandas package allows us to read and manipulate csv files.
import os
import pandas

csv_budget_data = os.path.join("Resources", "budget_data.csv")

   

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

# We must add 2 to correctly offset the month list to match the changes between months, which will be explain now: The first change is found by subtracting the first row in profits from the second row.  The first month can not have a change, as it is the initial value, and thus has nothing to subtract from it.  We therefore must add 1 to our month index to offset this difference; that is, the first change happens in the second month, the second change in the third month, etc.  We must also add 1 to our index again since the first row is the heading "Date," which puts the first month in the second row, the second month in the third row, etc.
max_change = max(changes)
max_change_index = changes.index(max(changes))
offset_max = max_change_index + 2

min_change = min(changes)
min_change_index = changes.index(min(changes))
offset_min = min_change_index + 2

print("Financial Analysis")
print("----------------------------")
print(f"Total months: {len(months)-1}")
print(f"Total profits: ${total_profit:,}")
print(f"Average Change: ${(sum(changes)/len(changes)):,.2f}")
print(f"Greatest Increase in Profits: {months[offset_max]} (${max(changes):,})")
print(f"Greatest Decrease in Profits: {months[offset_min]} (${min(changes):,})")