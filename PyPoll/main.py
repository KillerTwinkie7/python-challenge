import csv
import os

ballots = []    #| Store ballots, counties,
counties = []   #| and cadidates as lists from
candidates = [] #| the the file
i = 0 #| Counters. 'a' starts at 1 here because
a = 1 #| if it does not, the output file returns one vote too
x = 0 #| few when talllying everything up
winner = " "        #| Stores the name of the winner
winner_votes = 0    #| Initializes this value for future comparison

path = os.path.realpath(__file__) #|
directory = os.path.dirname(path) #| Got this bit of code from https://codeigo.com/python/get-directory-of-a-file/
print(directory)                  #|

with open(directory + "/Resources/election_data.csv") as file:
    csv_reader = csv.reader(file)                #| Open the file in question, and initialize
    for ballot, county, candidate in csv_reader: #| lists to store the data
        ballots.append(ballot)                   #|
        counties.append(county)                  #|
        candidates.append(candidate)             #|

ballots.remove(ballots[0])          #| Remove the header of the list before counting the elements. I omit
candidates.remove(candidates[0])    #| counties because I don't use that list.

candidates.sort() #Sort the list of candidates for easier iteration

#This step prints everything out to my output file.
with open(directory + "/Analysis/Poll Report.txt", 'w') as output:
    output.writelines("Election Results\n")             #|
    output.writelines("__________________\n")           #| Output the title and the total amount
    output.writelines(f"Total Votes: {len(ballots)}\n") #| of votes received.
    output.writelines("__________________\n")           #|

    for i in range(len(ballots) - 1): #Loop through each vote. The -1 is there for index purposes
        if candidates[i] != candidates[i+1]: #If things change, then do the following
            output.writelines(f"{candidates[i]} got {a} votes. {round((a / len(ballots))*100, 3)}%\n") #Print out the candidate name, the votes they received, and the percentage of votes they received.
            if a > winner_votes:        #| If the total number of votes received is higher than what's stored
                winner = candidates[i]  #| in the current winner's total, update the value and the name of the winner.
            a = 0 #Reset a to 0 to ensure you only count the specific candidate's votes
        if i == len(ballots) - 2: #Not gonna lie, not sure why I have to subtract 2 from the length here, but that's what worked *shrug*
            output.writelines(f"{candidates[i]} got {a+1} votes. {round((a / len(ballots))*100, 3)}%\n") #This whole bit of indexing is a mess holy cow
        i+=1 #| No infinite loops for me today
        a+=1 #| no siree
    
    output.writelines("__________________\n")   #| Finally, output the
    output.writelines(f"Winner: {winner}")      #| winner's name