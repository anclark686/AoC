import math

with open("day8data.txt", "r") as f:
    data = f.read().split("\n")

directions = list(data[0])

network = {}
for i in data[2:]:
    start, elements = i.split(" = ")
    network[start] = {"L": elements[1:4], "R": elements[6:9]}

def part_one(location, z_list):
    steps = 0
    
    while location not in z_list:
        direction = directions[0]
        directions.append(directions.pop(0))
        location = network[location][direction]
        steps += 1
    
    return steps

print(part_one("AAA", ["ZZZ"]))

def part_two():
    a_list = [x for x in network.keys() if x.endswith("A")]
    z_list = [x for x in network.keys() if x.endswith("Z")]
    total_steps = [part_one(x, z_list) for x in a_list]
    
    return math.lcm(*total_steps)

print(part_two())