# The data we need to retrieve
#1. The total number of votes to cast
#2. Complete list of candidates who received votes
#3. % of votes each candidate won
#4. total number of votes each candidate won
#5. Winner of election based on popular vote


# Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a diret or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Intialize a total vote counter and set it = to 0 to start
total_votes = 0 

# Declaring a new list with candidate names
candidate_options = []

# Declaring the empty dictinary uses {}
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and Print the header row
    headers = next(file_reader)
    

#Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1

     #Print candidate name for each row
        candidate_name = row[2]

        # If candidate does not match any existing candidate in list candidate_options
        if candidate_name not in candidate_options:
        # Add it to the list of candidates
            candidate_options.append(candidate_name)

        # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add to each candidate vote count
        candidate_votes[candidate_name] += 1

# Trying to find the percentage of votes for each candidate by looping through the counts       
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #2.  Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    #Create an if statement to determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
    #2. If true then set winning count = votes and winning percentage = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
    #3. Set the winning candidate = candidate name
        winning_candidate = candidate_name

    #Print statement to show the winning candidate
winning_candidate_summary = (f"--------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"------------------\n")
print(winning_candidate_summary)
    



