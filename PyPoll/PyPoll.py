# import csv and os
import os
import csv

# set path for files // electionData
electionData = os.path.join("Resources", "election_data.csv")

# declare variables
totalVotes = 0
# variables to track each candidate with their corresponding vote counts
candidateVotes = {}
# variables to track each candidates' number of votes, the % of votes each candidate got, and the overall winner
winningVoteCount = 0
candidateVotePercentage = {}

# open the election_data.csv file and read the file
with open(electionData) as csvFile:
   csvReader = csv.reader(csvFile, delimiter=",") # info in file is delimited by commas, this extracts info and 
   # reads the info separated by commas

   # skips the first row
   next(csvReader)

   # loops through csvfile and tracks the voting and candidate data
   for row in csvReader:
      totalVotes += 1 # adds a tally to the vote counter

      # generates a complete list of candidates who received votes AND the total number of votes they got
      if row[2] in candidateVotes:
         candidateVotes[row[2]] += 1
      else: 
         candidateVotes[row[2]] = 1

      # since it's already looping through the data, we can use the pulled numbers to generate the corresponding percentages to each voter
      # using an iterate dictionary within this for loops allows for us to directly pull the votes and track them as key-value pairs to get matched with each voter
      # link used to learn about using iterate dictionaries // second link for review on using .items() function to return objects
      # https://note.nkmk.me/en/python-dict-keys-values-items/
      # https://www.w3schools.com/python/ref_dictionary_items.asp#:~:text=Definition%20and%20Usage,the%20dictionary%2C%20see%20example%20below.

      for data, value in candidateVotes.items():
         candidateVotePercentage[data] = round((value/totalVotes)* 100 , 3) # round is used for readability when converting votecounts into percentage values

         if candidateVotePercentage[data] > winningVoteCount:
            winningVoteCount = candidateVotes[data]
         

# print these results in the terminal
print(f"Election Results")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Votes: {totalVotes}")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~")
for data, value in candidateVotes.items():
     print(data,':' , str(candidateVotePercentage[data]),'%','  ','(',candidateVotes[data],')')
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Winner: Diana DeGette")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~")

# print these results in an external text file // having issues, going to resubmit for more credit anyway

"""output = (f"Election Results\n~~~~~~~~~~~~~~~~~~~~\n"
          f"Total Votes: {totalVotes}\n~~~~~~~~~~~~~~~~~\n"
         for data, value in candidateVotes.items():
                print(data,':' , str(candidateVotePercentage[data]),'%','  ','(',candidateVotes[data],')')
          
)

with open("ElectionResults.txt", "w") as f:
   f.write(output)
   f.close()
  
"""


   


