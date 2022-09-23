tester = [
    {"Name": "Jeremy", "Age": 29, "Height": "5 feet 8 inches"},
    {"Name": "Tim", "Age": 30, "Height": "6 feet 0 inches"},
    {"Name": "Sarah", "Age": 27, "Height": "5 feet 5 inches"},
    {"Name": "Oliver", "Age": 24, "Height": "5 feet 10 inches"},
]


for i in tester:

    for j in i:
        print(f"{j}: {i[j]}", end=", ")
        "\n"
