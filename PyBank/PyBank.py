print(str("\nFinancial Analysis \n~~~~~~~~~~~~~~~~~~~~~~~~~"))
# prints the header for the PyBank Analysis code

# import csv files so they can be read in Python script
import os 
import csv

# set path for files
csvFilePath = os.path.join("Resources", "budget_data.csv")

# declare variables and lists
totalMonths = []
totalProfits = []
profitChanges = 0
monthlyChanges = []

with open(csvFilePath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    # the csvReader has the info in the file, split into rows of lists that correspond to each row of data in the file
    
    # skips the first row of csv file to not display title row
    next(csvReader)
    
    # read each row of data and display each row of data
    for row in csvReader:
      
# calculate total months
      totalMonths.append(row[0])
      totalProfits.append(row[1])
    #print(len(totalMonths)) # formatting issue with adding a string for "Total Months: " text
    print(f"Total Months: {len(totalMonths)}")
          
# calculate total profits
# the link below helped me better understand functions & list comprehensions
# https://realpython.com/python-return-statement/#:~:text=The%20Python%20return%20statement%20is,further%20computation%20in%20your%20programs.

    totalProfits = [int(x) for x in totalProfits]
    totalProfitSum = sum(totalProfits)
    print(f"Total Profits: {totalProfitSum}")

# changes in profit/losses over the entire period & the average
    for change in range(len(totalProfits)-1):
       monthlyChanges.append(totalProfits [change+1]-totalProfits[change])
       # the average needs to be sum of all profits/losses OVER the total amount of entries in the dataset - use sum for numerator and len for denom.
    avg = sum(monthlyChanges)/len(monthlyChanges)
    print("Average Change: ", avg)

# generating the max and min
maxProfit = max(monthlyChanges)
minProfit = min(monthlyChanges)
# .index() will allow us to access all the values from the dataset for use in finding the max and min
# read up on the site below to better understand using .index()
# https://www.simplilearn.com/tutorials/python-tutorial/index-in-python

maxProfitIndex = monthlyChanges.index(maxProfit)
minProfitIndex = monthlyChanges.index(minProfit)

print("Greatest Increase in Profits: ", totalMonths[maxProfitIndex + 1], maxProfit)
print("Greatest Decrease in Profit: ", totalMonths[minProfitIndex + 1], minProfit)

output = (f"Financial Analysis\n~~~~~~~~~~~~~~~~~~~~~~~\n"
        f"Total Months: {len(totalMonths)}\n"
          f"Total Profits: {totalProfitSum}\n"
          f"Average Change: {avg}\n"
          f"Greatest Increase in Profits: {maxProfit}\n"
          f"Greatest Decrease in Profits: {minProfit}\n"

)
with open ("PyBank.txt", "w") as f:
   f.write(output)
   f.close()




     

  


