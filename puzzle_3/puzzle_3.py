import string
from collections import Counter

lower_case_letters = list(string.ascii_lowercase)
upper_case_letters = list(string.ascii_uppercase)

letters = lower_case_letters + upper_case_letters
scores = {x: ind + 1 for ind, x in enumerate(letters)}

with open("puzzle_3/puzzle_3_input.txt", 'r') as file:
    sacks = [line.strip() for line in file.readlines()]
    priority_sum = 0
    elf = 0
    groups = []
    group = []

    for sack in sacks:
        group.append(sack)
        elf = elf + 1
        if elf == 3:
            groups.append(group)
            group = []
            elf = 0

    for group in groups:
        same = set(group[0]) & set(group[1]) & set(group[2])
        print(same)
        priority_sum = priority_sum + scores[list(same)[0]]
        
    print(priority_sum)
