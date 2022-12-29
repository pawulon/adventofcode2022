from pathlib import Path
from typing import List, Tuple

puzzle_input = Path('inputs/12').read_text()

heights: List[str] = puzzle_input.splitlines()
distances: List[List[int]] = []


def initialize_distances() -> None:
    for _ in range(len(heights)):
        distances.append([10000000 for _ in range(len(heights[0]))])


def get_starting_point() -> Tuple[int, int]:
    for y, line in enumerate(heights):
        if 'S' in line:
            starting_point_x = line.index('S')
            heights[y] = line.replace('S', 'a')
            return starting_point_x, y


def get_end_point() -> Tuple[int, int]:
    for y, line in enumerate(heights):
        if 'E' in line:
            end_point_x = line.index('E')
            return end_point_x, y


def get_end_point_distance() -> int:
    return get_distance(get_end_point())


def get_available_steps(point: Tuple[int, int]) -> List[Tuple[int, int]]:
    available_steps = []
    px, py = point
    for field in [(px + 1, py), (px - 1, py), (px, py - 1), (px, py + 1)]:
        test_point = (field[0], field[1])
        if step := test_step(test_point, current_letter=heights[py][px]):
            available_steps.append(step)

    return available_steps


def test_step(test_point: Tuple[int, int], current_letter: str) -> Tuple[int, int] | None:
    x, y = test_point
    if x < 0 or y < 0 or x > len(heights[0]) - 1 or y > len(heights) - 1:
        return None
    letter = heights[y][x]
    if letter == 'E':
        letter = 'z'
    if ord(letter) - ord(current_letter) <= 1:
        return x, y


def set_distance(point: Tuple[int, int], distance: int) -> None:
    distances[point[1]][point[0]] = distance


def get_distance(point: Tuple[int, int]) -> int:
    try:
        return distances[point[1]][point[0]]
    except IndexError:
        pass


def find_shortest_path_from_point(starting_point: Tuple[int, int]) -> int:
    initialize_distances()
    set_distance(starting_point, 0)
    points_to_check: List[Tuple[int, int]] = [starting_point]

    while True:
        if not points_to_check:
            return get_end_point_distance()
        current_point = points_to_check.pop()
        current_distance = get_distance(current_point)
        next_distance = current_distance + 1
        available_steps = get_available_steps(current_point)
        for available_step in available_steps:
            if get_distance(available_step) > next_distance:
                set_distance(available_step, next_distance)
                points_to_check.append(available_step)


# 12.1
print(find_shortest_path_from_point(starting_point=get_starting_point()))

# 12.2
path_lengths_for_all_starting_points = []
for y in range(len(heights)):
    shortest_path_length = find_shortest_path_from_point((0, y))
    path_lengths_for_all_starting_points.append(shortest_path_length)
print(min(path_lengths_for_all_starting_points))
