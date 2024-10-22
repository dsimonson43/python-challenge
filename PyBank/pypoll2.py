import os #imports operating system
import csv #imports csv capabilities

file_path = 'election_data.csv' #designates file path to election data csv

total_votes = 0 #initializes counter loop for total votes
candidates ={} #creates dictionary to store candidates and vote counts

with open(file_path, mode='r', newline='') as file: #opens the election_data csv file in reader mode and creates a new line, skips header
    csvreader = csv.reader(file)
    header = next(csvreader)
#increments total vote count by +1 for each row, extracts candidate name from column C whilst removing white space
    for row in csvreader:
        total_votes += 1
        candidate = row[2].strip()
#counts votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

results = f"\nElection Results\n--------------------------------\nTotal Votes: {total_votes}\n------------------------------------------\n"
winner = None #placeholder for no winner yet determined
max_votes = 0 #initializes counter loop for max votes
#establishes logic parameters for determining a winner and prints result
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"

    if votes > max_votes:
        max_votes = votes
        winner = candidate

results += f"---------------------------------\nWinner: {winner}\n-------------------------"
#creates a .txt file output
output_file = "election_results.txt"
with open(output_file, mode='w') as file:
    file.write(results)
    #print results and strips whitespace
print(results.strip())
