import csv as c
import os
from pathlib import Path

file_to_load = Path(
    "/Users/jeremy/Docs/School/Mod 3 PyPoll/Election_Analysis/Resources/election_results.csv"
)
file_to_save = Path(
    "/Users/jeremy/Docs/School/Mod 3 PyPoll/Election_Analysis/analysis/election_analysis.txt"
)

OS_File = os.path.join(
    "Users",
    "jeremy",
    "Docs",
    "School",
    "Mod 3 PyPoll",
    "Election_Analysis",
    "Resources",
    "election_results.csv",
)

OS_Save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

county_list = []
county_votes = {}

win_candidate = ""
win_count = 0
win_percent = 0

win_county = ""
win_county_votes = 0
win_county_percent = 0


with open(file_to_load) as election_data:
    file_reader = c.reader(election_data)

    header = next(file_reader)

    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

    with open(file_to_save, "w") as txtfile:

        election_results = (
            f"\nElection Results\n"
            f"---------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------\n"
        )
        print(election_results, end="")

        txtfile.write(election_results)

        for county in county_votes:
            cvotes = county_votes[county]
            cpercent = float(cvotes) / float(total_votes) * 100
            county_result = f"{county}: {cpercent:.1f}% ({cvotes})\n"
            print(county_result)
            txtfile.write(county_result)

            if (cvotes > win_county_votes) and (cpercent > win_county_percent):
                win_county_votes = cvotes
                win_county_percent = cpercent
                win_county = county

        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            percentage = float(votes) / float(total_votes) * 100
            candidate_results = f"{candidate}: {percentage:.1f}% ({votes})\n"
            print(candidate_results)
            txtfile.write(candidate_results)

            if (votes > win_count) and (percentage > win_percent):
                win_count = votes
                win_percent = percentage
                win_candidate = candidate
        winningsummary = (
            f"-----------------------\n"
            f"Winner: {win_candidate}\n"
            f"Winning vote Count: {win_count}\n"
            f"Winning Percentage: {win_percent:.1f}%\n"
            f"-----------------------------\n"
        )
        print(winningsummary)
        txtfile.write(winningsummary)
