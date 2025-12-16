with open("day_5\\inputs\\input.txt", "r") as file:
    raw_data = [line.strip("\n") for line in file.readlines()]


separator = raw_data.index("")
fresh_ranges = [
    (int(ranges.split("-")[0]), int(ranges.split("-")[1]))
    for ranges in raw_data[:separator]
]
available_ingredients = [int(id) for id in raw_data[separator + 1 :]]


def is_fresh(id: int) -> bool:
    for range in fresh_ranges:
        if range[0] <= id and id <= range[1]:
            return True
    return False


quantity = 0

for ingredient in available_ingredients:
    if is_fresh(ingredient):
        quantity += 1

print(quantity)
