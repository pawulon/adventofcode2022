from pathlib import Path

puzzle_input = Path('inputs/1').read_text()

calories_per_elf = []
current_calories_counter = 0
for line in puzzle_input.splitlines():
    if line:
        current_calories_counter += int(line)
        continue
    calories_per_elf.append(current_calories_counter)
    current_calories_counter = 0

calories_per_elf.append(current_calories_counter)
sorted_calories_per_elf = sorted(calories_per_elf, reverse=True)
# 1.1
print(sorted_calories_per_elf[0])
# 1.2
print(sum(sorted_calories_per_elf[:3]))
