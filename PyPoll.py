import csv as c
import os

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

    header = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txtfile:

        election_results = (
            f"\nElection Results\n"
            f"---------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------\n"
        )
        print(Results)
        txtfile.write(election_results)

        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            percentage = float(votes) / float(total_votes) * 100
            candidate_results = f"{candidate}: {percentage:.1f}% ({votes})\n"
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
        txtfile.write(winningsummary)
        # print(winningsummary)
