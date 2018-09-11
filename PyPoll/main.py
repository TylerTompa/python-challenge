# This os package allows us to create file paths across systems.
# The csv package allows us to read and write csv files.
# The pandas package allows us to manipulate csv files.
import os
import csv
import pandas

# This creates a file path leading to the election_data csv file so that users on different operating systems can use this file.
csv_election_data = os.path.join("Resources","election_data.csv")

# The pandas package allows us to create lists which are composed of individual rows from a csv file.
column_names = ["voter_id", "county", "candidate"]
votes = pandas.read_csv(csv_election_data, names=column_names, low_memory=False)
candidates= votes.candidate.tolist()

votes_correy = 0
votes_khan = 0
votes_li = 0
votes_otooley = 0
for i in range(len(candidates)):
    if candidates[i] == "Correy":
        votes_correy += 1
    if candidates[i] == "Khan":
        votes_khan += 1
    elif candidates[i] == "Li":
        votes_li += 1
    elif candidates[i] == "O'Tooley":
        votes_otooley += 1

# for i in candidates:
#     print(candidates[i])

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(candidates)-1}")
print("-------------------------")
print(f"Khan: {votes_khan}")
print(f"Correy: {votes_correy}")
print(f"Li: {votes_li}")
print(f"O'Tooley: {votes_otooley}")
