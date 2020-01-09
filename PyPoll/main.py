import os
import csv

path = "/Users/kevinkosumi12345/Genti/python-challenge/PyPoll/Resources/election_data.csv"
file = open(path, newline="")
reader = csv.reader(file)
header = next(reader)

# print(header)

# candidates that appear in column "Candidate" form a dictionary in which candidates are the dict.keys()
# first we have to create a Dictionary


candilist = {}

for row in reader:
   # row = ["Voter ID", "County", "Candidate"]
    # total number of rows = total number of votes
    candidate = row[2]
    if candidate in candilist.keys():
        candilist[candidate] += 1
    else:
        candilist[candidate] = 1
            
        print(candidate)

votes = candilist.values()
candidates = candilist.keys()
total_votes = sum(list(votes))

print(votes)
print(candidates)
print(total_votes)



