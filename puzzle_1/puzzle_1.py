with open('puzzle_1_input.txt') as file:
    elves = {}
    elf_counter = 0
    elf_calorie_list = []
    for line in file:
        
        if line == '\n':
            elves.update({elf_counter: elf_calorie_list})
            elf_counter += 1
            elf_calorie_list = []
            continue
        entry = line.strip('\n')
        elf_calorie_list.append(int(entry))

totals = set()
for elf, calories in elves.items():
    totals.add(sum(calories))

print(totals)

print(sum(sorted(totals, reverse=True)[:3]))
