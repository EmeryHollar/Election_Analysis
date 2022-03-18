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
# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Read and Print the header row
    headers = next(file_reader)
    print(headers)
#Print each row in the CSV file
    for row in file_reader:
        print(row)