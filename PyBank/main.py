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

    # Read through each row of data after the header
    for row in budgetfile:
        months.append(row[0])
        total += int(row[1])

    #Calculate monthly change
    for i in budgetfile:
    # Take the difference between two months and append to monthly profit change
        monthly_change.append(total[i+1]-total[i])
        
    #Find maximum and minimum monthly change
        max_increase_value = max(monthly_change)
        max_decrease_value = min(monthly_change)


    #print
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${(total)}")

    
    #save as .txt file
