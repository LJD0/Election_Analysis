import csv as c
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("Results", "election_results.txt")

with open(file_to_load) as Data1:
    file_reader = c.reader(Data1)
    for row in file_reader:
        print(row)
