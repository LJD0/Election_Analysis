import csv as c
import os
from unittest import skip

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("Results", "election_results.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

win_candidate = ""
win_count = 0
win_percent = 0


with open(file_to_load) as election_data:
    file_reader = c.reader(election_data)

    header = next(election_data)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = round((float(votes) / float(total_votes)) * 100, 1)
        print(f"{candidate}: {percentage:.1f}% ({votes})\n")
        if (votes > win_count) and (percentage > win_percent):
            win_count = votes
            win_percent = percentage
            win_candidate = candidate
    winningsummary = (
        "-----------------------------\n"
        f"the winning candidate is {win_candidate},\nwith a total of {win_count} votes,\ngathering {win_percent}% of the total votes"
        "\n-----------------------------"
    )

    print(winningsummary)
