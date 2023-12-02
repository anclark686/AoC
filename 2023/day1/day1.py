with open("day1data.txt", "r") as f:
    words = f.read().split("\n")

sum = 0

num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for word in words:
    nums = []
    
    # part two
    for num_word, num_val in num_dict.items():
        if num_word in word:
            word = word.replace(num_word, num_word[0:2] + num_val + num_word[2:])

    for char in word:
        if char.isdigit():
            nums.append(char)

    sum += int(nums[0] + nums[-1])

print(sum)