with open("day5data.txt", "r") as f:
  info = f.read().split("\n\n")

seeds = []
almanac = {}
seed_pairs = []
for i, line in enumerate(info): 
  title, nums = line.split(":")
  if i == 0:
    first_line = nums.strip().split(" ")
    seeds = {int(x): [int(x)] for x in first_line}
    pt_2_seeds = [int(x) for x in first_line if first_line.index(x) % 2 == 0]
    pt_2_ranges = [int(x) for x in first_line if first_line.index(x) % 2 != 0]
    seed_pairs = {pt_2_seeds[i]: pt_2_ranges[i] for i in range(len(pt_2_seeds))}
  else:
    almanac[title] = [[int(y) for y in x.split(" ")] for x in nums.strip().split("\n") ]

# part one
def traverse(seeds):
  for seed in seeds:
    for val in almanac.values():
      num_to_find = seeds[seed][-1]
      found = False
      for group in val:
        drs, srs, rl = group
        if num_to_find in range(srs, srs + rl):
          found = True
          seeds[seed].append(num_to_find + (drs - srs))
      if not found:
        seeds[seed].append(num_to_find)
  return seeds

locations = [x[-1] for x in traverse(seeds).values()]
print(min(locations))


# # part two
# pt2_seeds = {}
# for pair, ran in seed_pairs.items():
#   for x in range(pair, pair+ran):
#     pt2_seeds[x] = [x]

# pt_2_locations = [x[-1] for x in traverse(pt2_seeds).values()]
# print(pt_2_locations)
# print(min(pt_2_locations))