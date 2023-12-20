import re

with open("day18data.txt", "r") as f:
    data = f.read().split("\n")

dirs = []
lengths = []
colors = []

for line in data:
    print(line)
    direction, length, color = line.split(" ")
    dirs.append(direction)
    lengths.append(int(length))
    colors.append(re.sub(r'[\s()]', '', color))

matrix = [["." for x in range(len(dirs))] for y in range(len(dirs))]

print()
print(dirs)
print(lengths)
print(colors)
print()

for line in matrix:
    print(line)
print()

x, y = [0,0]

def mark_spot(x, y, matrix):
    matrix[x][y] = "#"
    return matrix

matrix = mark_spot(x, y, matrix)

for i in range(len(dirs)):
    direction = dirs[i]
    length = lengths[i]
    # print(length)
    if direction == "R":
        print("R")
        for j in range(length):
            y += 1
            matrix = mark_spot(x, y, matrix)
    elif direction == "D":
        print("D")
        for j in range(length):
            x += 1
            matrix = mark_spot(x, y, matrix)
    elif direction == "L":
        print("L")
        for j in range(length):
            y -= 1
            matrix = mark_spot(x, y, matrix)
    elif direction == "U":
        print("U")
        for j in range(length):
            x -= 1
            matrix = mark_spot(x, y, matrix)

for line in matrix:
    print(line)
print()

for i, line in enumerate(matrix):
    if "#" in line:
        start = line.index("#")
        end = len(line) - 1 - line[::-1].index("#")
        # print(line.index("#"))
        # print(line[::-1].index("#"))
        for j in range(start, end):
            matrix[i][j] = "#"
    else:
        break
    # for j, space in enumerate(line):
        

for line in matrix:
    print(line)
print()
print(sum(x.count("#") for x in matrix))