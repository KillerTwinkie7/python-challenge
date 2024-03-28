import csv
import os
import numpy

data = []       #|
i = 0           #| Variable initialization
months = []     #|
profit = []     #|
change = []     #| Stores the difference of each sequential data points
path = os.path.realpath(__file__) #|
directory = os.path.dirname(path) #| Got this bit of code from https://codeigo.com/python/get-directory-of-a-file/
print(directory)                  #|


with open(directory + "/Resources/budget_data.csv") as file:             #|
    csv_reader = csv.reader(file)    #| Open the file in question, and initialize
    for date, money in csv_reader:   #| lists to store the data
        months.append(date)          #|
        profit.append(money)         #|

monthHeader = months.pop(0) #| Take the first elements of those lists and
moneyHeader = profit.pop(0) #| remove them, and store them for later use maybe (I didn't actually use these later oops)

profit = [int(i) for i in profit] #Go through the list of profits and turn them all into integers so that I can add them together

j = 0                                       #|
for j in range(len(profit) - 1):            #| Calculate differences between each data point, and
    change.append(profit[j+1] - profit[j])  #| populate the 'change' list with those values.
    j+=1                                    #|

average = numpy.average(change) # Find the average change between sequential data points

high = max(change)                      #|
low = min(change)                       #| Find max and min values in the 'change' list, then find
high_index = change.index(max(change))  #| their indices to display later.
low_index = change.index(min(change))   #|

with open(directory + "/Analysis/Financial Report.txt", 'w') as output: #Open output file
    output.writelines("Financial Anaysis\n")                                                    #|
    output.writelines("_________________________________\n")                                    #| Pretty self-explanatory, but this
    output.writelines(f"Total Months: {len(months)}\n")                                         #| chunk outputs everything to a
    output.writelines(f"Total Amount Earned: ${sum(profit)}\n")                                 #| .txt file, while doing some light
    output.writelines(f"Average Change: ${average.round(2)}\n")                                 #| computations before doing so.
    output.writelines(f"Greatest Increase in Profits: {months[high_index + 1]} (${high})\n")    #|
    output.writelines(f"Greatest Decrease in Profits: {months[low_index + 1]} (${low})\n")      #|
file.close()   #| Apparently, it's good practice to close the files you're working with.
output.close() #| Who knew? Not me before Google 😎

# Not sure if this will affect things in the submission, but I installed numpy to my conda environment, so if you're running into issues, write >python s in the search bar
# and click Python: select interpreter. It should let you pick the right environment from there. Although, this is almost certainly a local usage thing, so it probably isn't an issue.