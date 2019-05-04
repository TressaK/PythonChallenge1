# import operating system module
import os
# import module to read csv files
import csv


csvpath = os.path.join ("Resources", "budget_data.csv")




with open (csvpath,'r',newline="") as csvfile:
    # csv reader identifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read header first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row of data after header
    for row in csvreader:

            print(row)



# Lists to store data
Total_Months = []
Net_Profit_Loss =[]
Average_Change =[]
Greatest_Profit_Loss =[]
Greatest_Profit_Increase =[]

