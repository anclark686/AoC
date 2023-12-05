import re
with open("day4data.txt", "r") as f:
  cards = f.read().split("\n")

def make_dict(cards):
  card_dict = {}
  for card in cards: 
    card_dict[int(re.search(r'\d+', card).group())] = {
      "winners": [int(x) for x in re.findall('[0-9]+', card[card.index(":"): card.index("|")])],
      "have": [int(x) for x in re.findall('[0-9]+', card[card.index("|"):])],
      "score": 0,
      "matches": 0,
      "instances": 1,
    }
  return card_dict

card_dict = make_dict(cards)

for game in card_dict:
  for num in card_dict[game]["have"]:
    if num in card_dict[game]["winners"]:
      if card_dict[game]["score"] == 0:
        card_dict[game]["score"] = 1
      else:
        card_dict[game]["score"] *= 2
      card_dict[game]["matches"] += 1
  for j in range(card_dict[game]["instances"]):
    for i in range(game + 1, game + card_dict[game]["matches"] + 1):
      card_dict[i]["instances"] += 1

print(sum([x["score"] for x in card_dict.values()]))
print(sum([x["instances"] for x in card_dict.values()]))