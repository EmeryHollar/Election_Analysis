# Election_Analysis
Using Python to analyze election data
# Overview of Election Audit
The main purpose of the election audit is by using Python in VS Code, determine which counties had the highest vote count and which candidate won the election. I was able to find out each county’s vote count and percentage of total votes as well as each candidates vote count and percentage of total votes. 

# Election-Audit Results
## How many votes were cast in this congressional election?
- 369,711
## Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. 
- As the image shows, Jefferson County had 38,855 votes making up 10.5% of the vote. Denver had 306,055 votes making up 82.8% of the vote. Arapahoe had 24,801 votes making up 6.7% of the vote. <img width="113" alt="County Vote Image" src="https://user-images.githubusercontent.com/100726716/159994813-013217a3-9a13-4b1c-94df-8135da3151b6.png">
## Which county had the largest number of votes?
- Denver with 306,055 votes. 
## Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- As the image shows, Charles Stockham had 85,213 votes making up 23.0% of the vote. Diana DeGette had 272,892 votes making up 73.8% of the vote. Raymon Doane had 11,606 votes making up 3.1% of the vote. <img width="155" alt="Candidate Vote Image" src="https://user-images.githubusercontent.com/100726716/159994567-6503c8b8-4793-44df-9e61-1459690bf20a.png">
## Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Diana DeGette won the election with 272,892 votes making up 73.8% of the total vote. <img width="110" alt="Winning Candidate" src="https://user-images.githubusercontent.com/100726716/159994887-635c9603-515e-4915-b29c-77e8c42150c3.png">

# Election-Audit Summary
This script can be modified slightly to be used for other elections by changing the csv file that is read in at the beginning of the script. If the csv is in the same format, but simply with different counties and candidates, the Python script will be able to read the change and find out the results for the different county. Also, if the csv file is read in with the candidate’s name and county name in different rows, you must modify the code on rows 52 and 55 to find the correct row. For example, in this csv the candidate’s names are in the 3rd row which is coded as [2], but if the candidate name in a different csv is in row 5, you would need to alter the code to [4]. 
