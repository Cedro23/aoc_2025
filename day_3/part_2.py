with open("day_3\\inputs\\input.txt", "r") as file:
    banks = [line.strip("\n") for line in file.readlines()]


def get_joltage(joltage: str, bank: str, depth: int) -> int:
    if depth == 0:
        return int(joltage)

    for i in range(9, 0, -1):
        index = bank.find(str(i))

        if index == -1 or index >= len(bank) - depth + 1:
            continue

        joltage += str(i)
        break
    return get_joltage(joltage, bank[index + 1 :], depth - 1)


joltages = []

for bank in banks:
    joltages.append(get_joltage("", bank, 12))

print(sum(joltages))
