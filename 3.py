from pathlib import Path

puzzle_input = Path('inputs/3').read_text()

rucksacks = [line for line in puzzle_input.splitlines()]


def calculate_priority(char: str) -> int:
    if char.islower():
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27


# 3.1
rucksacks_internals = [(rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]) for rucksack in rucksacks]
common_elements = [set(rucksack_internal[0]) & set(rucksack_internal[1]) for rucksack_internal in
                   rucksacks_internals]
priorities = [calculate_priority(common_element.pop()) for common_element in common_elements]
print(sum(priorities))

# 3.2
total_priority = 0
for i in range(0, len(rucksacks), 3):
    common_element = set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])
    total_priority += calculate_priority(common_element.pop())

print(total_priority)
