# imports
import os
import csv

# import csv
poll_csv = os.path.join('..', 'PyPoll', 'election_data.csv')

#
candidates = []
total_votes = []
candidate_votes = []
#
with open(poll_csv, newline="") as poll_data:
    election_data = csv.reader(poll_data, delimiter=',')
    header = next(election_data)    

# lists for variables

    for row in election_data:
        total_votes.append(row[0])

        if row[2] in candidates:
            candidates_index = candidates.index(row[2])
            candidate_votes[candidates_index] += 1
        
        else:
            candidates.append(row[2])
            candidate_votes.append(1)

vote_percentage = []
for count in range(len(candidates)):
    percentage = candidate_votes[count]/(len(total_votes))*100
    percentage = round(percentage)
    vote_percentage.append(percentage)

winner = max(candidate_votes)
index = candidate_votes.index(winner)
winning_candidate = candidates[index]

print("Election Results")
print("-------------------------")
print (f"Total Votes: {len(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(vote_percentage[i])}% ({str(candidate_votes[i])})")
print("-------------------------")
print (f"Winner: {winning_candidate}")
print("-------------------------")