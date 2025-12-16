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
        # Ignore odd size ids
        id_str = str(id)
        id_len = len(id_str)
        if id_len % 2 != 0:
            continue

        middle_index = int(id_len / 2)
        pattern = id_str[:middle_index]
        if pattern == id_str[middle_index:]:
            invalid_ids.append(id)

print(sum(invalid_ids))
