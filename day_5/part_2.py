with open("day_5\\inputs\\input.txt", "r") as file:
    raw_data = [line.strip("\n") for line in file.readlines()]


separator = raw_data.index("")
fresh_ids = [
    (int(ranges.split("-")[0]), int(ranges.split("-")[1]))
    for ranges in raw_data[:separator]
]

fresh_ids.sort(key=lambda tup: tup[0])
total_ids = 0

min_id = fresh_ids[0][0]
max_id = fresh_ids[0][1] + 1

for i in range(1, len(fresh_ids)):
    if max_id >= fresh_ids[i][0] + 1:
        max_id = max(max_id, fresh_ids[i][1] + 1)
        continue

    total_ids += max_id - min_id
    min_id = fresh_ids[i][0]
    max_id = fresh_ids[i][1] + 1

total_ids += max_id - min_id

print(total_ids)
