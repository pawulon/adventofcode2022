from pathlib import Path
from typing import Tuple, Set

puzzle_input = Path('inputs/4').read_text()

assignments = [line for line in puzzle_input.splitlines()]
assignment_pairs = [(assignment.split(',')[0], assignment.split(',')[1]) for assignment in assignments]


def is_full_overlap(assignment_pair: Tuple[str, str]) -> bool:
    assignment_ranges = get_assignment_ranges(assignment_pair)
    if assignment_ranges[0].issubset(assignment_ranges[1]) or assignment_ranges[0].issuperset(assignment_ranges[1]):
        return True
    return False


def is_overlap(assignment_pair: Tuple[str, str]) -> bool:
    assignment_ranges = get_assignment_ranges(assignment_pair)
    if assignment_ranges[0].intersection(assignment_ranges[1]):
        return True
    return False


def get_assignment_ranges(assignment_pair: Tuple[str, str]) -> Tuple[Set[int], Set[int]]:
    assignment_1, assignment_2 = assignment_pair
    assignment_1_start, assignment_1_end = assignment_1.split('-')
    assignment_2_start, assignment_2_end = assignment_2.split('-')
    return (set(range(int(assignment_1_start), int(assignment_1_end) + 1)),
            set(range(int(assignment_2_start), int(assignment_2_end) + 1)))


# 4.1
full_overlaps = [assignment_pair for assignment_pair in assignment_pairs if is_full_overlap(assignment_pair)]
print(len(full_overlaps))

# 4.2
overlaps = [assignment_pair for assignment_pair in assignment_pairs if is_overlap(assignment_pair)]
print(len(overlaps))
