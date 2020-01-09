import os
import csv



path = '/Users/kevinkosumi12345/Genti/python-challenge/PyBank/Resources/budget_data.csv'
budget_csv=os.path.join("../Resources", "budget_data.csv")
csvfile = open(path, newline="")

reader=csv.reader(csvfile, delimiter=",")
header = next(reader)
# print(header)

# the columns we have to convert into lists
# Create first 2 empty lists according 2 columns

date = []
profloss = []

# print("Financial Anaysis")
# print("-----------------------------------------")


for row in reader:
    date.append(row[0])
    profloss.append(int(row[1]))

# getting the total of Profit/Losses
total_profloss='Total Profit/Losses: $ ' + str(sum(profloss))
# print(total_profloss)

# getting the number of months in entire period
monthcount = 'Total months: ' + str(len(date))
# print(monthcount)

# before finding the averadge of change in Profit/Losses, first we have to find the total change
Total_change_profloss = 0
for x in range(1, len(profloss)):
    Total_change_profloss = Total_change_profloss + (profloss[x] - profloss[x-1])
    
# finding the averidge of change in Profit/Losses
avg_change_profloss = 'Averidge change in Profit/Loss: ' + str(round(Total_change_profloss/(len(profloss)-1),2))
# print(avg_change_profloss)

# getting the max value of data in Profit/Losses which is the Greatest Increase of Profit/Losses
maxVal = 'Greatest increase of Profit/Losses: '  + ' on ' + str(date[profloss.index(max(profloss))]) + ' $ ' + str(max(profloss))
# print(maxVal)

# the min Value of date in Profit/Losses which is the Greatest Decrease
minVal = 'Greatest decrease of Profit/Losses: ' + ' on ' + str(date[profloss.index(min(profloss))]) + ' $ ' + str(min(profloss))
# print(minVal)






DataBudget = open('csvfile.csv' , 'w')
DataBudget.write('Financial Analysus\n')
DataBudget.write('------------------------\n')
DataBudget.write(monthcount + '\n')
DataBudget.write(total_profloss + '\n')
DataBudget.write(avg_change_profloss + '\n')
DataBudget.write(maxVal + '\n')
DataBudget.write(minVal + '\n')
DataBudget.close