import re
from pathlib import Path

puzzle_input = Path('inputs/7').read_text()

filesystem = {}
current_folder = ''
at_most_100000 = []

for line in puzzle_input.splitlines():
    if line.startswith('dir ') or line == '$ ls':
        continue

    if match := re.match(r'\$ cd \.\.', line):
        child_folder_size = filesystem[current_folder]['TOTAL_SIZE']
        if child_folder_size <= 100000:
            at_most_100000.append(child_folder_size)
        current_folder = '/'.join(current_folder.split(r'/')[:-2]) + '/'
        filesystem[current_folder]['TOTAL_SIZE'] += child_folder_size

    elif match := re.match(r'\$ cd (.*)', line):
        current_folder += f'{match.group(1)}/'
        filesystem[current_folder] = {'TOTAL_SIZE': 0}

    else:
        match = re.match(r'(\d*) .*', line)
        file_size = int(match.group(1))
        filesystem[current_folder]['TOTAL_SIZE'] += file_size

last_folder_size = filesystem[current_folder]['TOTAL_SIZE']
if last_folder_size <= 100000:
    at_most_100000.append(child_folder_size)
# 7.1
print(sum(at_most_100000))

# 7.2
TOTAL_SPACE = 70000000
FREE_SPACE = TOTAL_SPACE - filesystem['//']['TOTAL_SIZE']
FREE_SPACE_RQUIRED = 30000000
SPACE_TO_FREE = FREE_SPACE_RQUIRED - FREE_SPACE

best_pick_so_far = TOTAL_SPACE
picked_folder = ''
for key, value in filesystem.items():
    if SPACE_TO_FREE <= value['TOTAL_SIZE'] < best_pick_so_far:
        best_pick_so_far = value['TOTAL_SIZE']
        picked_folder = key
print(picked_folder, best_pick_so_far)
