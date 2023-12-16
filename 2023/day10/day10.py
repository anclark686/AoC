with open("day10data.txt", "r") as f:
  matrix = [[y for y in list(x)] for x in f.read().split("\n")]

def find_s(matrix):
  s_loc = []
  for ti, x in enumerate(matrix):
    for ni, y in enumerate(x):
      if y == "S":
        s_loc = [ti, ni]
        break
    if len(s_loc) == 2:
      break
  return s_loc

main_s_loc = [[ti,ni] for ti,x in enumerate(matrix) for ni,y in enumerate(x) if y == "S"][0]
s_loc = main_s_loc

def find_neighbors(new_loc, distance):
  global matrix
  shape = matrix[new_loc[0]][new_loc[1]]
  matrix[new_loc[0]][new_loc[1]] = distance
  neighbors = {
    "west": matrix[new_loc[0]][new_loc[1]-1] if new_loc[1] != 0 else ".", # left
    "north": matrix[new_loc[0]-1][new_loc[1]] if new_loc[0] != 0 else ".", # top
    "east": matrix[new_loc[0]][new_loc[1]+1] if new_loc[1] != len(matrix[0]) -1 else ".", # right
    "south": matrix[new_loc[0]+1][new_loc[1]] if new_loc[0] != len(matrix) -1 else ".", # bottom
  }
  return neighbors, shape

neighbors, new_shape = find_neighbors(s_loc, 0)
neighbors_dirs = [x for x,y in neighbors.items() if y != "."]

shape_dict = {
  "-" : ["west", "east"],
  "|" : ["north", "south"],
  "J" : ["west", "north"],
  "7" : ["west", "south"],
  "L" : ["east", "north"],
  "F" : ["east", "south"],
}

def find_shape(neighbors_dirs):
  neighbors_dirs.sort()
  if neighbors_dirs == sorted(["west", "east"]):
    shape = "-"
  elif neighbors_dirs == sorted(["north", "south"]):
    shape = "|"
  elif neighbors_dirs == sorted(["west", "north"]):
    shape = "J"
  elif neighbors_dirs == sorted(["west", "south"]):
    shape = "7"
  elif neighbors_dirs == sorted(["east", "north"]):
    shape = "L"
  elif neighbors_dirs == sorted(["east", "south"]):
    shape = "F"

  return shape

def find_neighbors_dirs(neighbors):
  neighbors_dirs = []
  for i, (x, y) in enumerate(neighbors.items()):
    if y == ".":
      continue
    if i == 0 and (isinstance(y, int) or "east" in shape_dict.get(y)):
      neighbors_dirs.append("west")
    if i == 1 and (isinstance(y, int) or "south" in shape_dict.get(y)):
      neighbors_dirs.append("north")
    if i == 2 and (isinstance(y, int) or "west" in shape_dict.get(y)):
      neighbors_dirs.append("east")
    if i == 3 and (isinstance(y, int) or"north" in shape_dict.get(y)):
      neighbors_dirs.append("south")
  return neighbors_dirs

neighbors_dirs = find_neighbors_dirs(neighbors)
initial_shape = find_shape(neighbors_dirs)

def traverse(s_loc, distance, shape):
  if shape == "-": # ["west", "east"]
    if matrix[s_loc[0]][s_loc[1] + 1] == 0 or not isinstance(matrix[s_loc[0]][s_loc[1] + 1], int):
      s_loc = [s_loc[0], s_loc[1] + 1] # go east
    else:
      s_loc = [s_loc[0], s_loc[1] - 1] # go west
    neighbors, new_shape  = find_neighbors(s_loc, distance)
  elif shape == "L": # ["east", "north"]
    if matrix[s_loc[0]][s_loc[1] + 1] == 0 or not isinstance(matrix[s_loc[0]][s_loc[1] + 1], int):
      s_loc = [s_loc[0], s_loc[1] + 1] # go east
    else:
      s_loc = [s_loc[0] - 1, s_loc[1]] # go north
    neighbors, new_shape  = find_neighbors(s_loc, distance)
  elif shape == "|": # ["north", "south"]
    if matrix[s_loc[0] - 1][s_loc[1]] == 0 or not isinstance(matrix[s_loc[0] - 1][s_loc[1]], int):
      s_loc = [s_loc[0] - 1, s_loc[1]] # go north
    else:
      s_loc = [s_loc[0] + 1, s_loc[1]] # go south
    neighbors, new_shape  = find_neighbors(s_loc, distance)
  elif shape == "J": # ["west", "north"]
    if matrix[s_loc[0] - 1][s_loc[1]] == 0 or not isinstance(matrix[s_loc[0] - 1][s_loc[1]], int):
      s_loc = [s_loc[0] - 1, s_loc[1]] # go north
    else:
      s_loc = [s_loc[0], s_loc[1] - 1] # go west
    neighbors, new_shape  = find_neighbors(s_loc, distance)
  elif shape == "7": # ["west", "south"]
    if matrix[s_loc[0]][s_loc[1] - 1] == 0 or not isinstance(matrix[s_loc[0]][s_loc[1] - 1], int):
      s_loc = [s_loc[0], s_loc[1] - 1] # go west
    else:
      s_loc = [s_loc[0] + 1, s_loc[1]] # go south
    neighbors, new_shape  = find_neighbors(s_loc, distance)
  elif shape == "F": # ["east", "south"]
    if matrix[s_loc[0]][s_loc[1] + 1] == 0 or not isinstance(matrix[s_loc[0]][s_loc[1] + 1], int):
      s_loc = [s_loc[0], s_loc[1] + 1] # go east
    else:
      s_loc = [s_loc[0] + 1, s_loc[1]] # go south
    neighbors, new_shape = find_neighbors(s_loc, distance)
  return neighbors, s_loc, new_shape

distance = 1
neighbors, s_loc, new_shape = traverse(s_loc, distance, initial_shape)

while s_loc != main_s_loc:
  distance += 1
  neighbors, s_loc, new_shape = traverse(s_loc, distance, new_shape)

for x in matrix:
  print(x)
print(distance //2)

