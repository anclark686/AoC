with open("day13data.txt", "r") as f:
  data = [[list(x) for x in y.split("\n")] for y in f.read().split("\n\n")]

def check_horizontal(pattern):
  if len(pattern) % 2 != 0:
    pattern.append(pattern[0])

  start = 0
  index = 1
  middle = []
  final = []
  for i in range(len(pattern) - 1):
    if index != len(pattern):
      if pattern[start] == pattern[index]:
        middle = [start, index] if not middle else middle
        final = [start, index]
        start -= 1
        index += 1
      else:
        start += 1
        index += 1
  # print("middle")
  # print(middle)
  # print("final")
  # print(final)

  return middle[1] if middle else 0

def check_vertical(pattern):
  inverted = [[] for x in range(len(pattern[0]))]
  inverted_count = 0

  for i in range(len(pattern[0])):
    for j in range(len(pattern) -1, -1, -1):
      inverted[inverted_count].append(pattern[j][i])
    inverted_count += 1

  return check_horizontal(inverted)

def part_one(patterns):
  print("hello")
  count = 0
  for pattern in patterns:
    row_count = check_horizontal(pattern)
    print(f"row = {row_count}")
    col_count = check_vertical(pattern)
    print(f"col = {col_count}")
    print(row_count * 100 if row_count > col_count else col_count )
    print()
    count += row_count * 100 if row_count > col_count else col_count 
  print(count)

part_one(data)

# 13795 too low
# 34165 too low
# 40943 too high
