import csv

total_months = 0
total_profit_loss = 0
previous_value = None
changes= []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

csv_file_path = 'budget_data.csv'

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:

        date = row [0]
        profit_loss = row[1].strip()

        print(f"Date processed: {date}, Profit/Loss: {profit_loss}")
        

        try:
            profit_loss = int(profit_loss)
        except ValueError:
            continue

        total_months += 1
        total_profit_loss =+ profit_loss

        if previous_value is not None:
            change = profit_loss - previous_value
            changes.append(change)


            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]
           
        previous_value = profit_loss

if len(changes) >0:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0


output = (
"Financial Analysis\n"
"-----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_profit_loss}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(output)

with open('financial_analysis.txt', 'w') as txt_file:
    txt_file.write(output)