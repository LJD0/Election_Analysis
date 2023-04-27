from os import path
import csv


# Assign a variable for the file to load and the path.  
file_to_load = path.join("Election_Analysis", "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = path.join("Election_Analysis", "analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
county_options = []
candidate_results = []
county_results = []


# Declare the empty votes/percentages dictionaries.
candidate_votes = {}
candidate_percentage = {}
county_votes = {}
county_percentage = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
win_candidate_count = 0
win_candidate_percentage = 0
winning_county = ""
win_county_count = 0
win_county_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Find the candidate name from each row.
        candidate_name = row[2]
        # Find the county name from each row.
        county_name = row[1]
        # Create a list of candidates and initialize the votes for each candidate.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

    with open(file_to_save, "w") as results_file:

        # Create election reuslts header.
        election_results_header = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
        )

        # Determine the percentage of votes for each county by looping through the counts.
        for county_name in county_votes:
            # Retrieve vote count of a county.
            county_vote_count = county_votes[county_name]
            # Calculate the percentage of votes.
            county_percentage = (county_vote_count / total_votes) * 100
            # Create a variable to hold the county results.    
            result = f"{county_name}: received {county_percentage:.1f}% of the vote."
            county_results.append(result)
            # Determine winning vote count and county
            # Determine if the votes is greater than the winning count.
            if (county_vote_count > win_county_count) and (county_percentage > win_county_percentage):
                # If true then set winning_count = votes and winning_percent = vote_percentage.
                win_county_count = county_vote_count
                win_county_percentage = county_percentage
                # And, set the winning_county equal to the county's name.
                winning_county = county_name
            # Create a variable to hold the county win summary.
        county_win_summary = (
            f"County Vote Summary: \n"
            f"Highest Turnout: {winning_county}\n"
            f"Capturing {win_county_count:,} votes, {win_county_percentage:.1f}% of the total\n"
            f"-------------------------\n")
        

        # Determine the percentage of votes for each candidate by looping through the counts.
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            candidate_vote_count = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            candidate_percentage = (candidate_vote_count / total_votes) * 100
            # Create a variable to hold the candidate results.    
            result = f"{candidate_name}: received {candidate_percentage:.1f}% of the vote."
            candidate_results.append(result)
            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if (candidate_vote_count > win_candidate_count) and (candidate_percentage > win_candidate_percentage):
                # If true then set winning_count = votes and winning_percent = vote_percentage.
                win_candidate_count = candidate_vote_count
                win_candidate_percentage = candidate_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        # Create the winning candidate's summary variable.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {win_candidate_count:,}\n"
            f"Winning Percentage: {win_candidate_percentage:.1f}%\n"
            f"-------------------------\n")
        
        #Write the election results to the text file.
        results_file.write(election_results_header)
        results_file.write(county_win_summary)
        for result in county_results:
            results_file.write(result)
            results_file.write("\n")
        results_file.write(winning_candidate_summary)
        for result in candidate_results:
            results_file.write(result)
            results_file.write("\n")       
