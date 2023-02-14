print(str("\nElection Results\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
# import csv and os
import os
import csv

# declare variables
totalVotes = []
totalCandidates = []
candidatePercent = []
dataDictionary = {}
initiallyTotalledVotes = 0

# set path for files
csvFilePath = os.path.join("Resources", "election_data.csv")

with open(csvFilePath, "r") as csvFile:
   csvReader = csv.reader(csvFile)
   for row in csvReader:
      initiallyTotalledVotes += 1
      totalCandidates.append(row[2]) # attaching votes to corresponding candidates
      
      # create nested for loops to go through candidates and votes to find totalVotes
   for i in range(1, len(totalCandidates)):
      count = 0
      for j in range(len(totalVotes)):
         if totalCandidates[i]==totalVotes[j]:
            count += 1
            dataDictionary[totalCandidates[i]]==count
         totalCandidates.remove(totalCandidates[0])

         print(totalVotes)



