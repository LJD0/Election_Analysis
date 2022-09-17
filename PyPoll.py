import csv as c
import os
from unittest import skip

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("Results", "election_results.txt")

total_votes = 0

candidate_options = []


with open(file_to_load) as election_data:
    file_reader = c.reader(election_data)

    header = next(election_data)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

print(candidate_options)
