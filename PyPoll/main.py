import os
import csv

pathway = os.path.join('Resources', 'election_data.csv')

with open(pathway, encoding = "utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    csv_header = next(csv_reader)

    votes= []

    for rows in csv_reader:
        votes.append(rows[2])

election_results = {}

for vote in votes:
    
        if vote in election_results.keys():
            election_results[vote] = election_results[vote] + 1
    
        else:
            election_results[vote] = 1

print()
print("Election Results")
print()
print("-------------------------")
print()
print("Total Votes: ", len(votes))
print()
print("-------------------------")
print()
print("Charles Casper Stockham: ", 
((election_results["Charles Casper Stockham"]) / (len(votes)))*100, 
election_results["Charles Casper Stockham"])
print()
print("Diana DeGette: ", 
((election_results["Diana DeGette"]) / (len(votes)))*100, 
election_results["Diana DeGette"])
print()
print("Raymon Anthony Doane: ", 
((election_results["Raymon Anthony Doane"]) / (len(votes)))*100, 
election_results["Raymon Anthony Doane"])
print()
print("-------------------------")
print()
print("Winner: Diana DeGette")

output_path = os.path.join("Analysis", "analysis.txt")

with open(output_path,"w") as analysis:
    analysis.write('Election Results \n')
    analysis.write('\n')
    analysis.write('------------------------- \n')
    analysis.write('\n')
    analysis.write(f'Total Votes: {len(votes)}')
    analysis.write('\n')
    analysis.write('------------------------- \n')