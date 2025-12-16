with open("day_4\\inputs\\input.txt", "r") as file:
    grid = [list(line.strip("\n")) for line in file.readlines()]

height = len(grid)
width = len(grid[0])


def check_neighbors(x: int, y: int) -> bool:
    neighbors = 0
    if x - 1 >= 0 and grid[y][x - 1] == "@":
        neighbors += 1
    if x + 1 < width and grid[y][x + 1] == "@":
        neighbors += 1
    if y - 1 >= 0 and grid[y - 1][x] == "@":
        neighbors += 1
    if y + 1 < height and grid[y + 1][x] == "@":
        neighbors += 1
    if x - 1 >= 0 and y - 1 >= 0 and grid[y - 1][x - 1] == "@":
        neighbors += 1
    if x - 1 >= 0 and y + 1 < height and grid[y + 1][x - 1] == "@":
        neighbors += 1
    if x + 1 < width and y - 1 >= 0 and grid[y - 1][x + 1] == "@":
        neighbors += 1
    if x + 1 < width and y + 1 < height and grid[y + 1][x + 1] == "@":
        neighbors += 1
    return neighbors < 4


result = 0

for i in range(0, height):
    for j in range(0, width):
        if grid[i][j] == ".":
            continue

        # Check neighboring cells
        if check_neighbors(j, i):
            result += 1

print(result)
