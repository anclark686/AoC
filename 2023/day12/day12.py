import re

with open("day12data.txt", "r") as f:
  data = f.read().split("\n")

conditions = {}
counter = 0
iterations = 0
for line in data:
  line = line.split(" ")
  conditions[counter] = {
    "springs": line[0],
    "records": [int(x) for x in line[1].split(",")]
  }
  # print(conditions[counter])
  counter += 1

  springs = line[0]
  records = [int(x) for x in line[1].split(",")]
  hashes = ["#" * int(x) for x in line[1].split(",")]
  print(springs)
  print(records)
  # print(hashes)
  groups = re.findall(r"([\?(?!#)]+|[.]+)", springs)
  print(groups)

  to_check = records[:]
  print(to_check)
  print("Ready")
  prev = []
  changed = False
  for i, x in enumerate(groups):
    if "?" in x:
      y = next((x for x in to_check if isinstance(x, int)), None)

      if len(x) == y:
        to_check[to_check.index(y)] = "x"
        groups[i] = y * "#"
        changed = True
        continue

      print(to_check)
      while y:
        if "#" in x:
          pieces = re.findall(r"([\?]+|[#]+)", springs)
          print(pieces)
          print(pieces)
          print()
          # for a, piece in enumerate(pieces):
            

        if x.count("?") >= y:
          x = x.replace("?", "#", y)
          if "?" in x:
            x = x.replace("?", ".", 1)
          to_check[to_check.index(y)] = "x"
        else:
          break
        groups[i] = x
        changed = True
        y = next((x for x in to_check if isinstance(x, int)), None)


    elif "#" in x:
      if len(x) in to_check:
        to_check[to_check.index(len(x))] = "x"

      print(to_check)
    prev = x

  print(to_check)
  print(groups)
  final = re.findall(r"[#]+", "".join(groups))
  if final == hashes:
    iterations += 1
  
  print(final)
  print(iterations)
  

  # for i, x in enumerate(groups):
  #   if "?" in x:
  #     print(x)
  #     y = next((x for x in records if isinstance(x, int)), None)
  #     while y:
  #       iterations += 1
  #       print(y)
  #       if y and x.count("?") >= y:
  #         x = x.replace("?", "#", y)
  #         print(x)
  #         if "?" in x:
  #           x = x.replace("?", ".", 1)
  #           print(x)
  #         records[records.index(y)] = "x"
  #       else:
  #         break
  #       y = next((x for x in records if isinstance(x, int)), None)
      
  #   elif "#" in x:
  #     y = next((x for x in records if isinstance(x, int)), None)
  #     records[records.index(y)] = "x"
  #   groups[i] = x
  #   print(records)
  #   print("".join(groups))




  #   for j, y in enumerate(records):
  #     if y != "x" and ():
  #       print(x)
  #       print(y)
  #       x[:y] = "#"
  #       print(x)
  #       print()
  #       records[j] = "x"
  #   print(records)

  
  print()
  
print(iterations)

print()
print(conditions)