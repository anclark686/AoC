import os
from datetime import date

print(os.getcwd())
today = date.today().strftime("%d")
print(today)

for i in range(1, int(today) + 1):
  folder = f"{os.getcwd()}/day{i}"

  if not os.path.exists(folder):
    os.makedirs(folder)
    with open(f"{folder}/day{i}.py", "w") as f:
      pass
    with open(f"{folder}/day{i}instructions.txt", "w") as f:
      pass
    with open(f"{folder}/day{i}data.txt", "w") as f:
      pass


