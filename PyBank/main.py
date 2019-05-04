# import operating system module
import os
# import module to read csv files
import csv

# define where to find the file
csvpath = os.path.join ("Resources", "budget_data.csv")



# open the file
with open (csvpath,'r') as csvfile:
    # csv reader reads file and identifies break between columns
    csvreader = csv.reader(csvfile, delimiter=',')

    # moves to next to line
    next(csvreader)
    
    # Lists to store data
    Months = []
    Profit_Loss =[]
    
    # loop through each row
    for row in csvreader:
        
        # add months and profit info to lists
        Months.append (row [0])
        Profit_Loss.append (int(row[1]))

    # variables
Total_Months = len(Months)
Net_Profit_Loss = sum(Profit_Loss)
print(Total_Months, Profit_Loss)

# List of changes
Changes = []

# calculate greatest increase
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""


# create loop for change 
for index in range(1, len(Profit_Loss)):
    change = Profit_Loss[index] -(Profit_Loss[index -1])
    Changes.append(change) 
    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_date = Months[index]

    if change < greatest_decrease:
        greatest_decrease = change
        greatest_decrease_date = Months[index]

#greatest increase
print(greatest_increase_date)
print(greatest_increase)
print(greatest_decrease)
print(greatest_decrease_date)

# calculate average change
avg_change = sum(Changes)/len(Changes)
print(avg_change)
avg_change_rounded = round(avg_change, 2)




# find date of greatest increase

# datetime.date index
# calculate greatest decrease 
greatest_decrease = min(Changes)
print(greatest_decrease)

    
    

# find date of greatest decrease



# print('Financial Analysis')
# print('-------------------')

# print(f"Total Months:{Total_Months}")





