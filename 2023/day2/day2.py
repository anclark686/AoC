from functools import reduce

game_dict = {}

with open("day2data.txt", "r") as f:
    for line in f:
        game, colors = line.strip().split(":", 1)
        game = int("".join([x for x in game if x.isdigit()]))
        game_dict[game] = [[{k:int(v) for k,v in [y.split(" ")[::-1]]} for y in x.strip().split(", ")] for x in colors.strip().split(";")]

color_dict = {"red": 12, "green": 13, "blue": 14}
game_nums = []
part_two_dict = {}

for game, subsets in game_dict.items():
    bad_game = []
    part_two_dict[game] = {"red": 0, "green": 0, "blue": 0}

    for subset in subsets:
        shall_not_pass = []
        for colors in subset:
            if colors.get("red"):
                part_two_dict[game]["red"] = colors.get("red") if colors.get("red") > part_two_dict[game]["red"] else part_two_dict[game]["red"]
                if colors.get("red") > color_dict["red"]:
                  shall_not_pass.append("bad")
            if colors.get("green"):
                part_two_dict[game]["green"] = colors.get("green") if colors.get("green") > part_two_dict[game]["green"] else part_two_dict[game]["green"]
                if colors.get("green") > color_dict["green"]:
                  shall_not_pass.append("bad")
            if colors.get("blue"): 
                part_two_dict[game]["blue"] = colors.get("blue") if colors.get("blue") > part_two_dict[game]["blue"] else part_two_dict[game]["blue"]
                if colors.get("blue") > color_dict["blue"]:
                  shall_not_pass.append("bad")
        if shall_not_pass:
            bad_game.append("bad")
    if not bad_game:
        game_nums.append(game)

print(sum(game_nums))

part_two_sum = 0

for game, colors in part_two_dict.items():
    part_two_sum += reduce(lambda a, b: a*b, colors.values())

print(part_two_sum)

