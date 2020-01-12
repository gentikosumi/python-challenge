import os
import csv

path = "/Users/kevinkosumi12345/Genti/python-challenge/PyPoll/Resources/election_data.csv"
file = open(path, newline="")
reader = csv.reader(file)
header = next(reader)

# print(header)

# candidates that appear in column "Candidate" form a dictionary in which candidates are the dict.keys()
# first we have to create a Dictionary


print('Election Results')
print('---------------------------------')



candilist = {}

for row in reader:
   # row = ["Voter ID", "County", "Candidate"]
    # total number of rows = total number of votes
    candidate = row[2]
    if candidate in candilist.keys():
        candilist[candidate] += 1
    else:
        candilist[candidate] = 1
            
       # print(candidate)

votes = candilist.values()
candidates = candilist.keys()
total_votes = sum(list(votes))


total_votes_count = 'Total votes : ' + str(sum(list(votes)))

# print('---------------------------------')

# Finding values for each key of our dictionary
d_items = candilist.items()

for key, value in candilist.items():
    percentage=round(((value/total_votes)*100),2)
    candidates_with_votes = key+' : '+ str(percentage)+'% ' +'('+str(value)+')'
    print(candidates_with_votes)
    # print(key, ' : ', percentage, '%', '(',value,')')


print('---------------------------------')

# Finding the key with the max value in our dictionary
v = list(candilist.values())
k = list(candilist.keys())
Winner = 'Winner ' + (k[v.index(max(v))])
print(Winner)
print('---------------------------------')


#Writing the csv file (Printing the Results)

csv_columns = ['key', 'percentage', 'value']
dict = candilist

Results = open('results.csv' , 'w')

Results.write('Election Results\n')
Results.write('------------------------\n')
Results.write(total_votes_count + '\n')
Results.write('------------------------\n')
writer = csv.writer(Results)
for key in dict:
    percentage=round(((dict[key]/total_votes)*100),2)
    writer.writerow([key + ' : ' + str(percentage)+'% ' + '('+str(dict[key])+')'])

   
Results.write('------------------------\n')
Results.write(Winner + '\n')
Results.write('------------------------\n')

Results.close()




