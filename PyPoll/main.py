# This os package allows us to create file paths across systems.
# The csv package allows us to read and write csv files.
# The pandas package allows us to manipulate csv files.
import os
import csv
import pandas
from statistics import mode

# This creates a file path leading to the election_data csv file so that users on different operating systems can use this file.
csv_election_data = os.path.join("Resources","election_data.csv")

# The pandas package allows us to create lists which are composed of individual rows from a csv file.
column_names = ["voter_id", "county", "candidate"]
votes = pandas.read_csv(csv_election_data, names=column_names, low_memory=False)
candidates= votes.candidate.tolist()

# This loop iterates through out list of candidates and adds one vote each time the candidate's name is found.
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

# This creates a list, and stores therein the percent of votes each candiate recieves.  We divide the the number of votes for each candidate by one less than the length of the list, since the first row of the list is a header. 
vote_percentages = []

percent_votes_correy = round((100*(votes_correy/(len(candidates)-1))),3)
percent_votes_khan = round((100*(votes_khan/(len(candidates)-1))),3)
percent_votes_li = round((100*(votes_li/(len(candidates)-1))),3)
percent_votes_otooley = round((100*(votes_otooley/(len(candidates)-1))),3)

vote_percentages.append(percent_votes_correy)
vote_percentages.append(percent_votes_khan)
vote_percentages.append(percent_votes_li)
vote_percentages.append(percent_votes_otooley)

#Stackoverflow says this could cause problems if more than one value appears the maximum number of times.
winner = mode(candidates)

# Someone suggested using the pandas mode function.  Ask about this in class.
# candidates_dataframe = pandas.DataFrame(candidates)
# winner = candidates_dataframe.mode(axis=0)

# This prints the results.
print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(candidates)-1}")
print("-------------------------")
print(f"Khan: {percent_votes_khan}% ({votes_khan})")
print(f"Correy: {percent_votes_correy}% ({votes_correy})")
print(f"Li: {percent_votes_li}% ({votes_li})")
print(f"O'Tooley: {percent_votes_otooley}% ({votes_otooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
