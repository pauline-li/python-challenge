import os
import csv


#C:\Users\pli.TELOS\Desktop\Bootcamp\VS Python Code\Lecture3

bank_csv = os.path.join('../PyBank/budget_data.csv')

row_count = 0
total = 0


with open(bank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
     

    FirstFlag = True   

    #for x in bank_csv

    for bank_data in csvreader:
         date = str(bank_data[0])
         profitloss = int(bank_data[1])
         if FirstFlag == True:
            min_date = date
            min_profitloss = profitloss 
            FirstFlag = False
         total = total + profitloss
         row_count += 1   #

    max_date = date
    max_profitloss = profitloss
  



 
    print(f"Financial Analysis") 
    print(f"----------------------------".center(24," ")) 
    print(f"Total Months: {str(row_count)}")
    print(f"Total: ${str(total)}")
    print(f"Min Date: {min_date} Max Date: {max_date}")
    print(f"Average Change: ${str(round((max_profitloss-min_profitloss)/(row_count-1), 2))}")  


 