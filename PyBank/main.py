#imports
import os
import csv

#import csv
budget_csv = os.path.join('..', 'PyBank', 'budget-data.csv')

#create lists for variables
months = []
monthly_change = []
with open(budget_csv, newline="") as csvfile:

# Split the data on commas
    budgetfile = csv.reader(csvfile, delimiter=',')
    header = next(budgetfile)
    total = 0
    month_revenue = 0

# Read through each row of data after the header
    for row in budgetfile:
        months.append(row[0])
        total += int(row[1])
        
# Take the difference between two months and append to monthly profit change
        monthly_change.append(int(row[1]) - month_revenue)
        month_revenue = int(row[1])
        
#Find maximum and minimum monthly change
    #Greatest increase in profits
        max_increase = max(monthly_change)
        best_index = monthly_change.index(max_increase)
        best_date = months[best_index]

    #Greatest decrease (lowest increase) in profits 
        max_decrease = min(monthly_change)
        worst_index = monthly_change.index(max_decrease)
        worst_date = months[worst_index]

    #Get Average Change
        change_total = sum(monthly_change) - 867884
        total_months = len(months)
        avg_change = round(change_total/total_months, 2)

#print statements
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${(total)}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {best_date} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(max_decrease)})")

# save to .txt file
filepath = os.path.join("output_pybank.txt")
with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Total Months: {len(months)}" + "\n")
    text.write(f"Total: ${(total)}" + "\n")
    text.write(f"Average Change: ${avg_change}" + "\n")
    text.write(f"Greatest Increase in Profits: {best_date} (${str(max_increase)})" + "\n")
    text.write(f"Greatest Decrease in Profits: {worst_date} (${str(max_decrease)})" + "\n")