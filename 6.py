from pathlib import Path

puzzle_input = Path('inputs/6').read_text()

# 6.1
for i in range(len(puzzle_input) - 3):
    if len(set(puzzle_input[i:i + 4])) == 4:
        break
print(i + 4)

# 6.2
for i in range(len(puzzle_input) - 13):
    if len(set(puzzle_input[i:i + 14])) == 14:
        break
print(i + 14)
