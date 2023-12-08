with open("day7data.txt", "r") as f:
  data = f.read().split("\n")

hand_dict = {
  "g_5_oak": [],
  "f_4_oak": [],
  "e_full": [],
  "d_3_oak": [],
  "c_2_pair": [],
  "b_1_pair": [],
  "a_high": []
}

# part one
# faces = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

# part two
faces = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
ranks = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
rank_dict = dict(map(lambda a,b: (a,b), faces, ranks))

def find_type(hand):
  hand_type = ""
  distinct = list(set(hand))
  set_len = len(distinct)
  no_js = hand.replace("J", "")

  # part two
  if "J" in hand and faces[-1] == "J": # last conditional checks if pt 2
    for i in distinct:
      if (hand.count(i) > 1 or len(no_js) == set_len - 1) and i != "J":
        hand = hand.replace("J", i)
        break
    distinct = list(set(hand))
    set_len = len(distinct)

  if set_len == 1:
    hand_type = "g_5_oak"
  elif set_len == 5:
    hand_type = "a_high"
  elif set_len == 4:
    hand_type = "b_1_pair"
  elif set_len == 2:
    if hand.count(distinct[0]) == 4 or hand.count(distinct[1]) == 4:
      hand_type = "f_4_oak"
    else:
      hand_type = "e_full"
  elif set_len == 3:
    card1_count = hand.count(distinct[0])
    card2_count = hand.count(distinct[1])
    card3_count = hand.count(distinct[2])
    if card1_count == 3 or card2_count == 3 or card3_count == 3:
      hand_type = "d_3_oak"
    else:
      hand_type = "c_2_pair"

  return hand_type

card_dict = {}
for i, line in enumerate(data):
  hand, bid = line.split(" ")
  hand_type = find_type(hand)
  card_dict[hand] = {"hand": hand, "bid": bid, "type": hand_type, "rank": 0}
  hand_dict[hand_type].append(hand)

def order(a):
  return tuple(rank_dict[y] for y in a)

for hand_type, hand_list in hand_dict.items():
  if len(hand_list) > 1:
    hand_dict[hand_type] = sorted(hand_list, key=order)

rank = 1
def assign_rank(hand):
  global rank
  card_dict[hand]["rank"] = rank
  rank += 1

for i in sorted(hand_dict.keys()):
  for j in hand_dict[i]:
    assign_rank(j)

print(sum([x["rank"] * int(x["bid"]) for x in card_dict.values()]))