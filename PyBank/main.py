import os 
import csv

file = os.path.join('budget_data' + '.csv')

bank = {}

total_months = 0

with open("budget_data.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader, None)

    