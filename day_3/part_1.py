with open("day_3\\inputs\\input.txt", "r") as file:
    banks = [line.strip("\n") for line in file.readlines()]

joltages = []

for bank in banks:
    for i in range(9, 1, -1):
        index = bank.find(str(i))
        if index == -1 or index == len(bank) - 1:
            continue

        first = i
        break

    short_bank = bank[index + 1 :]
    for i in range(9, 1, -1):
        index = short_bank.find(str(i))
        if index == -1:
            continue

        second = i
        break

    joltages.append(int(f"{first}{second}"))

print(sum(joltages))
