#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#----------------------------------------
#Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a vote counter
total_votes = 0 

#Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Track the Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #2. add to the total vote count
        total_votes += 1
    
    #Get the candidate name from each row
        candidate_name = row[2] 

    #if the candidate does not match any existing candidate add to the candidate list
        if candidate_name not in candidate_options:
    
    #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

    # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
    
    #3. Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
        
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
            #2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            #3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            
            #4. Print the candidate's name, vote count, and percentage of votes to the terminal
            candidate_results = (f"{candidate_name} :  {vote_percentage:.1f} % ({votes:,})\n")
            
             # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            #1. Determine winning vote count, winning percentage, and winning candidate
            if (votes> winning_count) and (vote_percentage > winning_percentage):
                #2. If true then set winning_count = votes and winning_percent = #vote percentage
                winning_count = votes
                #3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
                winning_percentage = vote_percentage
                
                 
            
            #Printing out winning candidate's results to the terminal.
            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
            print(winning_candidate_summary)
            # Save the winning candidate's name to the text file.
            txt_file.write(winning_candidate_summary)