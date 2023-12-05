import re
from string import punctuation
from functools import reduce

with open("day3data.txt", "r") as f:
    rows = f.read().split("\n")

matrix = []
for x in rows:
    matrix_row = []
    row_nums = re.findall(r"\d+", x)

    for i, y in enumerate(x):
        num = ""
        num_found = False
        if not y.isdigit():
            matrix_row.append(y)
        else:
            if num_found:
                continue
            elif row_nums and x[i: i + len(row_nums[0])] == row_nums[0]:
                for a in range(0, len(row_nums[0])):
                    matrix_row.append(row_nums[0])
                num_found = True
                row_nums.pop(0)
    matrix.append(matrix_row)

num_list = []
gear_list = []
for i, row in enumerate(matrix):
    for j, entry in enumerate(row):
        if entry in punctuation and entry != ".":
            left = row[j-1].replace(".", "") if j != 0 else ""
            t_left = matrix[i-1][j-1].replace(".", "") if i != 0 and j != 0 else ""
            top = matrix[i-1][j].replace(".", "") if i != 0 else ""
            t_right = matrix[i-1][j+1].replace(".", "") if i != 0 and j != len(row) - 1 else ""
            right = row[j+1].replace(".", "") if j != len(row) - 1 else ""
            b_right = matrix[i+1][j+1].replace(".", "") if i != len(matrix) - 1 and j != len(row) - 1 else ""
            bottom = matrix[i+1][j].replace(".", "") if i != len(matrix) -1 else ""
            b_left = matrix[i+1][j-1].replace(".", "") if i != len(matrix) -1 and j != 0 else "" 
            
            neighbors = [
                left,
                t_left if t_left != top else "",
                top,
                t_right if t_right != top else "",
                right,
                b_right if b_right != bottom else "",
                bottom,
                b_left if b_left != bottom else "",
            ]
            neighbor_dict = {
                "left": left,
                "tl": t_left,
                "top": top,
                "tr": t_right,
                "right": right,
                "br": b_right,
                "bottom": bottom,
                "bl": b_left
            }
            num_neighbors = [int(x) for x in neighbors if x.isdigit()]
            num_list.extend(num_neighbors)
            print(num_neighbors)
            if entry == "*" and len(num_neighbors) == 2:
                gears = reduce(lambda a,b: a*b, num_neighbors)
                gear_list.append(gears)

print(sum(num_list))
print(sum(gear_list))
