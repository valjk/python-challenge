# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
budget_csv = os.path.join('/Users/valkeeranan/Desktop/python-challenge/PyBank/Resources/budget_data.csv')  # Input file path
analysis_txt = os.path.join('/Users/valkeeranan/Desktop/python-challenge/PyBank/analysis/budget_analysis.txt')  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
month_of_change = []
net_change_list = []

# Open and read the csv
with open(budget_csv) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    # Track the total and net change
    # Process each row of data
    # Track the total
    # Track the net change
    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the average net change across the months
    net_monthly_average = round(sum(net_change_list) / len(net_change_list), 2)

# Generate the output summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_average}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(analysis_txt, "w") as txt_file:
    txt_file.write(output)
