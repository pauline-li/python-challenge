import os
import csv

bank_csv = os.path.join('../PyBank/budget_data.csv')
total = 0

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') # Split the data on commas
    header = next(csvreader)
     
    change_to_profit_loss =[] 
    increase_date =[] 
    grt_increase = 0
    FirstFlag = True   

   
    for bank_data in csvreader:
         date = str(bank_data[0])
         profitloss = int(bank_data[1])
         if FirstFlag == True:
            min_date = date
            min_profitloss = profitloss 
            FirstFlag = False
         total = total + profitloss
         change_to_profit_loss.append(profitloss)
         increase_date.append(date)


    list_length = len(increase_date)-1
    greatest_inc= change_to_profit_loss[1]-change_to_profit_loss[0] 
    greatest_dec= change_to_profit_loss[1]-change_to_profit_loss[0] 
    incr_month=0
    decr_month=0

    for i in range(1,list_length+1):
        change=change_to_profit_loss[i] - change_to_profit_loss[i-1] 
        if change > greatest_inc:
            greatest_inc = change 
            incr_month = i 
        if change < greatest_dec:
            greatest_dec = change 
            decr_month = i

        
    print(f"Financial Analysis") 
    print(f"----------------------------".center(24," ")) 
    print(f"Total Months: {len(increase_date)}")
    print(f"Total: ${str(total)}")
    print(f"Average Change: ${str(round((change_to_profit_loss[list_length]-change_to_profit_loss[0])/list_length, 2))}")
    print(f"Greatest Increase in Profits: {increase_date[incr_month]} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {increase_date[decr_month]} (${greatest_dec})")


csv_writer = output_path = os.path.join("../PyBank/PyBank_Output.csv")  # Write and create file in here

with open(csv_writer, 'w') as csvfile:

    # Initialize csv.writer
    csv_writer = csv.writer(csvfile)
    #csvfile.write("\n".join("Financial Analysis"))

    # Write the first row (column headers)
   
    csv_writer.writerow(["Financial Analysis"])
    csv_writer.writerow(["----------------------------".center(24," ")])
    csv_writer.writerow([f"Total Months: {len(increase_date)}"])
    csv_writer.writerow([f"Total: ${str(total)}"])
    csv_writer.writerow([f"Average Change: ${str(round((change_to_profit_loss[list_length]-change_to_profit_loss[0])/list_length, 2))}"])
    csv_writer.writerow([f"Greatest Increase in Profits: {increase_date[incr_month]} (${greatest_inc})"])
    csv_writer.writerow([f"Greatest Decrease in Profits: {increase_date[decr_month]} (${greatest_dec})"])

