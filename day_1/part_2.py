# This time the password is the amount of times the dial points at 0 (not just stops)
with open("day_1\\inputs\\input.txt", "r") as file:
    instructions = file.readlines()

instructions = [(line[0], int(line[1:])) for line in instructions]

pos = 50
password = 0

for direction, steps in instructions:
    for i in range(steps):
        pos += -1 if direction == "L" else 1
        pos = pos % 100
        if pos == 0:
            password += 1


print(password)
