import os
import csv

bank_csv = os.path.join('Resources', 'budget_data.csv')

months = []
profit_loss = []
profit_loss_change = []

with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    csv_header = next(csv_reader)

    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
    
    for i in range(len(profit_loss)-1):
        profit_loss_change.append(profit_loss[i + 1] - profit_loss[i])

total_months = len(months)
profit = sum(profit_loss)
average_change = round(sum(profit_loss_change)/len(profit_loss_change),2)
max_change = max(profit_loss_change)
min_change = min(profit_loss_change)

print()
print('Financial Analysis')
print()
print('-------------------------')
print()
print("Total Months:", total_months)
print()
print (f'Total: ${profit}')
print()
print(f'Average Change: ${average_change}')
print()
print(f'Greatest Increase in Profits: ${max_change}')
print()
print(f'Greatest Decrease in Profits: ${min_change}')

output_path = os.path.join("Analysis", "analysis.txt")

with open(output_path,"w") as analysis:
    analysis.write('Financial Analysis \n')
    analysis.write('\n')
    analysis.write('------------------------- \n')
    analysis.write('\n')
    analysis.write(f'Total Months: {total_months} \n')
    analysis.write('\n')
    analysis.write(f'Total: ${profit}\n')
    analysis.write('\n')
    analysis.write(f'Average Change: ${average_change}\n')
    analysis.write('\n')
    analysis.write(f'Greatest Increase in Profits: ${max_change}\n')
    analysis.write('\n')
    analysis.write(f'Greatest Decrease in Profits: ${min_change}')