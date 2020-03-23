import os
import csv
import datetime

#C:\Users\pli.TELOS\Desktop\Bootcamp\VS Python Code\Lecture3

bank_csv = os.path.join('../PyBank/budget_data.csv')

row_count = 0

with open(bank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
    for bank_data in csvreader:
        date = str(bank_data[0])
        profitloss = int(bank_data[1])
        row_count += 1 

print(f"Financial Analysis".center(24," ")) 
print(f"----------------------------".center(24," ")) 
print(f"Total Months: {str(row_count)}")

        


   
    # for bank_data in csvreader:
    #     date = str(bank_data[0])
    #     profitloss = int(bank_data[1])
    #     if float(bank_data[1]) >= 569899:
    #         print(f"date {date} amount {profitloss}")


#     def average(numbers):  # no need to explicity define as list
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total/length



# print(average([1,5,9]))
# print(average(range(11)))


 