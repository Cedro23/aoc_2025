from operator import mul
from functools import reduce

with open("day_6\\inputs\\input.txt", "r") as file:
    raw_data = [
        list(filter(None, line.strip("\n").split(" "))) for line in file.readlines()
    ]

operators = []
numbers = []

for i in range(len(raw_data[-1])):
    operators.append(raw_data[-1][i])
raw_data.pop()

for j in range(len(operators)):
    numbers.append([int(item[j]) for item in raw_data])

result = 0

for n in range(len(operators)):
    if operators[n] == "*":
        result += reduce(mul, numbers[n], 1)
    elif operators[n] == "+":
        result += sum(numbers[n])

print(result)
