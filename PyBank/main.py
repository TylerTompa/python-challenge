# The os package allows us to create files paths across different operating systems.
# The csv package allows us to read and write to csv files.
import os
import csv

# This creates a file path leading to the budget_data csv file so that users on different operating systems can use this file.
csv_budget_data = os.path.join("Resources", "budget_data.csv")

# Later we will use a for-loop to create a list of profits and months using the columns from our csv file.  This is to initialize those lists so that we may use the append() method.
months = []
profits = []

# This reads the budget_data csv file and uses a for loop to create lists composed of the contents from each column.
with open(csv_budget_data,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        months.append(row[0])
        profits.append(row[1])

""" We will create a variable called total_profit, then we will use a for-loop to add the profit from every month, which will result in the total profit across every month.  We must ensure that we do not include the first row, as this is a heading and thus a string object."""
total_profit = 0
for i in range(len(profits)):
    if i != 0:
        total_profit += int(profits[i])

""" The variable changes is a list which stores the change in profits for each month.  The suceeding for-loop will find the difference between each pair of adjancent months and store them in this list.  We will then be able to use primitive functions to find the sum and length of this list, and thereafter the average.  Again we must ensure not to include the first row, as this is a column heading and thus a string object."""
changes = []
for i in range(len(profits)):
    if i not in (0,1):
        change = int(profits[i]) - int(profits[i-1])
        changes.append(change)

average_change = round(sum(changes)/len(changes),2)

""" We must add 2 to correctly offset the month list to match the changes between months, which will be explained now: The first change is found by subtracting the first row in profits from the second row.  The first month can not have a change, as it is the initial value, and thus has nothing to subtract from it.  We therefore must add 1 to our month index to offset this difference; that is, the first change happens in the second month, the second change in the third month, etc.  We must also add 1 to our index again since the first row is the heading "Date," which puts the first month in the second row, the second month in the third row, etc.""" 
greatest_profit_increase_index = changes.index(max(changes))
offset_greatest_increase = greatest_profit_increase_index + 2

greatest_profit_decrease_index = changes.index(min(changes))
offset_greatest_decrease = greatest_profit_decrease_index + 2

# This prints the financial statistics we found.
print("Financial Analysis")
print("----------------------------")
print(f"Total months: {len(months)-1}")
print(f"Total profits: ${total_profit:,}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {months[offset_greatest_increase]} (${max(changes):,})")
print(f"Greatest Decrease in Profits: {months[offset_greatest_decrease]} (${min(changes):,})")

# This creates a file path which a text file with the analysis will be exported to.
text_export = os.path.join("financial_analysis.txt")

# This creates a text file with the analysis and exports it to the path defined above.
with open(text_export, "w", newline="") as txt_file:
    csv_writer = csv.writer(txt_file)

    csv_writer.writerow(["Financial Analysis"])
    csv_writer.writerow(["----------------------------"])
    csv_writer.writerow([f"Total months: {len(months)-1:,}"])
    csv_writer.writerow([f"Total profits: ${total_profit:,}"])
    csv_writer.writerow([f"Average Change: ${average_change:,}"])
    csv_writer.writerow([f"Greatest Increase in Profits: {months[offset_greatest_increase]} (${max(changes):,})"])
    csv_writer.writerow([f"Greatest Decrease in Profits: {months[offset_greatest_decrease]} (${min(changes):,})"])