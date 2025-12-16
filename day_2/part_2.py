import csv

with open("day_2\\inputs\\input.csv", mode="r") as file:
    csvFile = csv.reader(file)
    id_ranges = [
        (int(ranges.split("-")[0]), int(ranges.split("-")[1]))
        for ranges in next(csvFile)
    ]

invalid_ids = []

for ids in id_ranges:
    for id in range(ids[0], ids[1] + 1):
        # Check invalid ids
        id_str = str(id)
        id_len = len(id_str)

        for i in range(1, int(id_len / 2) + 1):
            pattern = id_str[:i]
            occurrences = id_str.count(pattern)
            if occurrences == id_len / i:
                invalid_ids.append(id)
                break

print(sum(invalid_ids))
