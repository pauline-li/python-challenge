import os
import csv
import datetime

#C:\Users\pli.TELOS\Desktop\Bootcamp\VS Python Code\Lecture3

bank_csv = os.path.join('../PyBank/budget_data.csv')



with open(bank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
  
   
    for bank_data in csvreader:
        date = str(bank_data[0])
        profitloss = int(bank_data[1])
        if float(bank_data[1]) >= 569899:
            print(f"date {date} amount {profitloss}")


 