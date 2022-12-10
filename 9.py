from dataclasses import dataclass
from pathlib import Path

puzzle_input = Path('inputs/9').read_text()


@dataclass
class Move:
    direction: str
    steps: int


commands = puzzle_input.splitlines()
moves = [Move(command.split()[0], int(command.split()[1])) for command in commands]


def initialize_line(line_length):
    return [(0, 0) for _ in range(line_length + 1)]


def move_point(point, direction):
    if direction == 'U':
        return point[0], point[1] + 1
    if direction == 'D':
        return point[0], point[1] - 1
    if direction == 'L':
        return point[0] - 1, point[1]
    if direction == 'R':
        return point[0] + 1, point[1]


def should_tail_move(head_position, tail_position):
    if abs(head_position[0] - tail_position[0]) > 1 or abs(head_position[1] - tail_position[1]) > 1:
        return True
    return False


def new_tail_position(head_position, tail_position):
    x_diff = (head_position[0] - tail_position[0]) / 2
    y_diff = (head_position[1] - tail_position[1]) / 2
    if abs(x_diff) == 0.5:
        x_diff *= 2
    if abs(y_diff) == 0.5:
        y_diff *= 2
    return tail_position[0] + x_diff, tail_position[1] + y_diff


def count_visited_places(line_length: int):
    line = initialize_line(line_length)
    visited_places = {(0, 0)}
    for move in moves:
        for i in range(move.steps):
            new_point = move_point(line[-1], move.direction)
            line[-1] = new_point
            for knot_index in range(line_length - 1, -1, -1):
                if should_tail_move(line[knot_index + 1], line[knot_index]):
                    line[knot_index] = new_tail_position(line[knot_index + 1], line[knot_index])
                    if knot_index == 0:
                        visited_places.add(line[knot_index])
    return len(visited_places)


print(count_visited_places(line_length=1))
print(count_visited_places(line_length=9))
