print(str("\nElection Results\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"))
# import csv and os
import os
import csv

# declare variables
totalVotes = []

# set path for files
csvFilePath = os.path.join("Resources", "election_data.csv")

with open(csvFilePath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #skip the first row of csv file to not display title row
    next(csvReader)



    #read each row of data and display each row of data
    for row in csvReader:
        totalVotes.append(row[0]) # find the total amount of votes from the election
        
    print(f"Total Votes: {len(totalVotes)}")

    # get list of unique candidates
    candidateGroupByCount = csvReader.groupby(["Candidate"]).count()["Voter ID"]

    candidateList = list(candidateGroupByCount)
        