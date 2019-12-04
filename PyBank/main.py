# import os 
# import csv

# file = os.path.join('budget_data' + '.csv')

# bank = {}

# total_months = 0

# with open("budget_data.csv", 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     next(csv_reader, None)

#     total_months += 1
#     if row[0] in bank.keys():
#         bank[row[0]] = bank[row[0]] + 1

import os
import csv

file = os.path.join('budget_data' + '.csv')

total_months = 0
months_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
total_net = 0 

with open("budget_data.csv",'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    header = next(csv_reader)

    first_row = next(csv_reader)
    total_months += 1 
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    for row in csv_reader:
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        months_change = months_change + [row[0]]
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    
net_monthly_avg = sum(net_change_list)/len(net_change_list)



output = (
    f"\nFinancial Analysis\n"
  f"----------------------------\n"
  f"Total Months: {total_months}\n"
  f"Total: ${total_net}\n"
  f"Average  Change: ${net_monthly_avg}\n"
  f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
  f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)
output_file = os.path.join( 'budget_data' + '.txt')

print(output)

with open(output_file, 'w') as write_file:
    write_file.write(output)

    