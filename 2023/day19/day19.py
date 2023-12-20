import re
with open("day19data.txt", "r") as f:
    workflows, ratings = [x.split("\n") for x in f.read().split("\n\n")]


workflows_dict = {}
for x in workflows:
    split_list = x.replace("}", "").split("{")
    k, v = split_list

    v = v.split(",")
    default = v[-1]
    v.pop()
    
    conditionals = {}
    for i in v:
        conditional, n = i.split(":")
        a, b, c = re.split(r"(<|>)", conditional)
        conditionals[a] =  [b, int(c), n]
    
    workflows_dict[k] = {"cond": conditionals, "default": default}


rating_dict = {x: {} for x in range(len(ratings))}
for i, x in enumerate(ratings):
    for y in x.split(","):
        f, g = y.split("=")
        rating_dict[i][re.sub(r"[{}]", "", f)] = int(re.sub(r"[^\w]", "", g))


def find_next(v, cond, default):
    op, num, n = cond
    if op == "<":
        if v < num:
            return n
    elif op == ">":
        if v > num:
            return n
    return default


total = 0
ends = ["R", "A"]
for key, val in rating_dict.items():
    index = "in"
    poss_next = workflows_dict[index]["default"]

    while poss_next not in ends:
        cond = workflows_dict[index]["cond"]
        poss_next = workflows_dict[index]["default"]

        counter = 0
        for k, v in val.items():
            if cond.get(k):
                n = find_next(v, cond.get(k), poss_next)

                if n != poss_next:
                    poss_next = n
                    break
                counter += 1

        index = poss_next

    if poss_next == "A":
        total += sum(val.values())

print(total)

# 385672 too high