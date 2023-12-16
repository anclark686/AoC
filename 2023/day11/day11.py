with open("day11data.txt", "r") as f:
  matrix = [[y for y in list(x)] for x in f.read().split("\n")]

universe = []
num = 1
galaxy_ind = []
for i, x in enumerate(matrix):
  universe.append(x)
  if not "#" in x:
    universe.append(x[:])
  for j, y in enumerate(x):
    if y == "#":
      galaxy_ind.append(j)
      matrix[i][j] = num
      num += 1

missing = [x for x in range(len(universe[0])) if x not in galaxy_ind]

for ind, x in enumerate(universe):
  counter = 0
  for i in missing:
    universe[ind].insert(i + counter, ".")
    counter += 1

pairs = [(i, j) for i in range(1, num) for j in range(i + 1, num)]

sums = 0

for pair in pairs:
  loc1 = [[ti,ni] for ti,x in enumerate(universe) for ni,y in enumerate(x) if y == pair[0]][0]
  loc2 = [[ti,ni] for ti,x in enumerate(universe) for ni,y in enumerate(x) if y == pair[1]][0]
  x_axis = loc2[0] - loc1[0] if loc2[0] > loc1[0] else loc1[0] - loc2[0]
  y_axis = loc2[1] - loc1[1] if loc2[1] > loc1[1] else loc1[1] - loc2[1]

  sums += x_axis + y_axis

print(sums)

