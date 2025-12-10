# Dial from 0 to 99 in order (modulo 100)
# Instructions start with 'L' or 'R'
# followed by a number indicating how many steps to turn the dial
# Dial starts at 50
# Password is the number of times the dial lands on 0.

# open instructions file
with open("day_1\part_1\input.txt", "r") as file:
    instructions = file.readlines()

# separate instructions into list of tuples (direction, steps)
instructions = [(line[0], int(line[1:])) for line in instructions]

pos = 50
password = 0

for direction, steps in instructions:
    pos = (pos - steps) % 100 if direction == "L" else (pos + steps) % 100
    if pos == 0:
        password += 1

print(password)
