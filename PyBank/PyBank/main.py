# Import necessary modules
import os
import csv
import statistics

# Create Path to File
budget_data = os.path.join("..", "PyBank","Resources", "budget_data.csv")

# Initalize Variables
total = []
months = []
month_change = []

# Make Calculation for average
def average (numbers):
    total = 0.0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average
    
with open(budget_data)as csvfile:
    
    # Specify CSV delimiter
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvfile)
    
    #Append the Rows
    for row in csvreader:
        months.append(row[0])
        total.append(row[1])
        month_change.append(int(row[1]))

    # Find the net amount of profits/losses
    total_revenue =0
    for values in total:
        total_revenue += int(values)
    print(f'Total Profits/Losses: ${total_revenue}')
    net_revenue = [j-i for i,j in zip(month_change[:-1], month_change[1:])]
    print(f'Average Change: ${round(average(net_revenue),2)}')
    net_revenue.sort(reverse=True)

    print(f'Total Months: {len(months)}') 
    print(f'Greatest Increase In Profits: (${net_revenue[0]})')           
    print(f'Greatest Decrease In Profits: (${net_revenue[len(net_revenue)-1]})')
        
    #Output the path
    output_path = "Finacial Analysis.txt"
with open(output_path,'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["---------------------------------------------------"])
    csvwriter.writerow([f'Total Months: {len(months)}'])
    csvwriter.writerow([f'Total Profits/Losses: ${total_revenue}'])
    csvwriter.writerow([f'Average Change: ${round(average(net_revenue),2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits:(${net_revenue[0]})'])
    csvwriter.writerow([f'Greatest Decrease in Profits:(${net_revenue[len(net_revenue)-1]})'])
    
    