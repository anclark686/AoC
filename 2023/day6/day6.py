import re
from functools import reduce

with open("day6data.txt", "r") as f:
  data = f.read().split("\n")

times, distances = [[int(y) for y in re.findall(r"\d+", x)] for x in data]
time2, distance2 = [[y for y in re.findall(r"\d+", x)] for x in data]

race_dict = {}

# part one
for i in range(len(times)):
  race_dict[i+1] = {"time": times[i], "distance": distances[i], "nums_to_win": []}

# part two 
race_dict = {0: {"time": int("".join(time2)), "distance": int("".join(distance2)), "nums_to_win": []}}

num_ways_to_win = []
for race, val in race_dict.items():
  for i in range(1, val["time"]):
    secs_left = val["time"] - i
    total = i * secs_left
    if total > val["distance"]:
      val["nums_to_win"].append(i)
  num_ways_to_win.append(len(val["nums_to_win"]))

print(reduce(lambda a,b: a*b, num_ways_to_win))
