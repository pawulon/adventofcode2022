import re
from pathlib import Path
from typing import NamedTuple

stacks = [
    ['B', 'G', 'S', 'C'],
    ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'],
    ['M', 'Q', 'S'],
    ['B', 'S', 'L', 'T', 'W', 'N', 'M'],
    ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'],
    ['C', 'T', 'B', 'G', 'Q', 'H', 'S'],
    ['T', 'J', 'P', 'B', 'W'],
    ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'],
    ['N', 'S', 'H', 'B', 'P', 'F']
]

puzzle_input = Path('inputs/5').read_text()


class Move(NamedTuple):
    count: int
    start: int
    end: int


moves = []
for line in puzzle_input.splitlines():
    pattern = r'move (\d*) from (\d*) to (\d*)'
    match = re.match(pattern, line)
    moves.append(Move(count=int(match.group(1)), start=int(match.group(2)) - 1, end=int(match.group(3)) - 1))

# 5.1
for move in moves:
    src_stack = stacks[move.start]
    dst_stack = stacks[move.end]
    for i in range(move.count):
        dst_stack.append(src_stack.pop())

message = ''.join([stack[-1] for stack in stacks])
print(message)

# 5.2
stacks = [
    ['B', 'G', 'S', 'C'],
    ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'],
    ['M', 'Q', 'S'],
    ['B', 'S', 'L', 'T', 'W', 'N', 'M'],
    ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'],
    ['C', 'T', 'B', 'G', 'Q', 'H', 'S'],
    ['T', 'J', 'P', 'B', 'W'],
    ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'],
    ['N', 'S', 'H', 'B', 'P', 'F']
]

for move in moves:
    src_stack = stacks[move.start]
    dst_stack = stacks[move.end]
    crates_to_be_moved = []
    for i in range(move.count):
        crates_to_be_moved.append(src_stack.pop())
    dst_stack += reversed(crates_to_be_moved)

message = ''.join([stack[-1] for stack in stacks])
print(message)
