# This time the password is the amount of times the dial points at 0 (not just stops)
with open("day_1\\inputs\\input.txt", "r") as file:
    instructions = file.readlines()

instructions = [(line[0], int(line[1:])) for line in instructions]

pos = 50
password = 0

for direction, steps in instructions:
    new_pos = pos - steps if direction == "L" else pos + steps

    # We don't count when we start from zero and don't move at least a full turn
    if pos == 0 and steps < 100:
        pos = new_pos % 100
        continue

    password += abs(new_pos // 100)

    if direction == "L":
        if new_pos % 100 == 0:  # ending on 0
            password += 1
        elif new_pos % 100 != 0 and pos == 0:  # starting on 0 and not ending on 0
            password -= 1

    pos = new_pos % 100

print(password)
