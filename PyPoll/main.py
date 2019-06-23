# imports
import os
import csv

# import csv
poll_csv = os.path.join('..', 'PyPoll', 'election_data.csv')

# set list variables
candidates = []
total_votes = []
candidate_votes = []
# read csv
with open(poll_csv, newline="") as poll_data:
    election_data = csv.reader(poll_data, delimiter=',')
    header = next(election_data)    

# calculate total votes by appending total_votes by row
    for row in election_data:
        total_votes.append(row[0])
# build lis of all candidates: if candidate exists, add to current index of votes
#   if not, add candidate and append candidates list to include candidate
#       and append candidate_votes list to include new vote count
        if row[2] in candidates:
            candidates_index = candidates.index(row[2])
            candidate_votes[candidates_index] += 1
        
        else:
            candidates.append(row[2])
            candidate_votes.append(1)
# set list for percentages
vote_percentage = []
# for each candidate in the candidates list, calculate percentage of votes
for count in range(len(candidates)):
    percentage = candidate_votes[count]/(len(total_votes))*100
    percentage = round(percentage)
    vote_percentage.append(percentage)
# set winner as max votes, set winning_candidate to the candidate sharing that index
winner = max(candidate_votes)
index = candidate_votes.index(winner)
winning_candidate = candidates[index]

# print statements
print("Election Results")
print("-------------------------")
print (f"Total Votes: {len(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(vote_percentage[i])}% ({str(candidate_votes[i])})")
print("-------------------------")
print (f"Winner: {winning_candidate}")
print("-------------------------")

# save to .txt file
filepath = os.path.join("output_pypoll.txt")
with open(filepath,'w') as text:
    text.write("Election Results" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Total Votes: {len(total_votes)}" + "\n")
    text.write("-------------------------" + "\n")
    for i in range(len(candidates)):
        text.write(f"{candidates[i]}: {str(vote_percentage[i])}% ({str(candidate_votes[i])})" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Winner: {winning_candidate}" + "\n")
    text.write("-------------------------" + "\n")