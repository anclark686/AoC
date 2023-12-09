with open("day9data.txt", "r") as f:
  data = [[int(y) for y in x.split(" ")] for x in f.read().split("\n")]

pt1_values = []
pt2_values = []

for row in data:
  all_rows = [row]
  next_row = []
  while set(next_row) != {0}:
    next_row = []
    for i in range(1, len(row)):
      next_row.append(row[i] - row[i-1])
    all_rows.insert(0, next_row)
    row = next_row

  for i, seq in enumerate(all_rows):
    if i == 0:
      all_rows[i].append(0)
    else:
      end_val = seq[-1] + all_rows[i-1][-1]
      beg_val = seq[0] - all_rows[i-1][0]
      all_rows[i].append(end_val)
      all_rows[i].insert(0, beg_val)

      if i + 1 == len(all_rows):
        pt1_values.append(end_val)
        pt2_values.append(beg_val)

print(sum(pt1_values))
print(sum(pt2_values))