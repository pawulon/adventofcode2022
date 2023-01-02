from pathlib import Path
from pprint import pprint
from typing import Tuple, List

puzzle_input = Path('inputs/14').read_text().splitlines()


def initialize_rocks() -> List[List[Tuple[int, int]]]:
    rocks = []
    for line in puzzle_input:
        rocks.append([eval(coordinates) for coordinates in line.split(' -> ')])
    return rocks


def get_rocks_min_max_indices(rocks: List[List[Tuple[int, int]]]) -> Tuple[int, int, int, int]:
    min_x = min_y = 1000000
    max_x = max_y = 0
    for rock_line in rocks:
        for coordinate in rock_line:
            if coordinate[0] > max_x:
                max_x = coordinate[0]
            if coordinate[0] < min_x:
                min_x = coordinate[0]
            if coordinate[1] > max_y:
                max_y = coordinate[1]
            if coordinate[1] < min_y:
                min_y = coordinate[1]
    return min_x, min_y, max_x, max_y


def initialize_scan_map(min_x: int, max_x: int, max_y: int) -> List[List[str]]:
    width = max_x - min_x + 3
    height = max_y + 2
    scan = []
    for _ in range(height):
        scan.append([' ' for _ in range(width)])
    return scan


def normalize_rocks(rocks: List[List[Tuple[int, int]]], min_x: int) -> None:
    for i, rock_line in enumerate(rocks):
        for j, coordinate in enumerate(rock_line):
            rocks[i][j] = (coordinate[0] - min_x, coordinate[1])


def add_rocks_to_scan(scan: List[List[str]], rocks: List[List[Tuple[int, int]]]) -> None:
    for rock_line in rocks:
        for i in range(len(rock_line) - 1):
            line_start, line_end = determine_start_point(point_1=rock_line[i], point_2=rock_line[i + 1])
            line_length = get_line_length(line_start, line_end)
            if is_horizontal_line(point_1=line_start, point_2=line_end):
                for j in range(line_length):
                    scan[line_start[1]][line_start[0] + j + 1] = 'x'
            else:
                for j in range(line_length):
                    scan[line_start[1] + j][line_start[0] + 1] = 'x'


def add_rock_floor(scan: List[List[str]]) -> None:
    scan.append(['x' for _ in range(len(scan[-1]))])


def extend_scan(scan: List[List[str]], margin: int) -> None:
    for y in range(len(scan)):
        scan[y] = [' ' for _ in range(margin)] + scan[y] + [' ' for _ in range(margin)]


def is_horizontal_line(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> bool:
    return point_1[1] == point_2[1]


def determine_start_point(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> Tuple[
    Tuple[int, int], Tuple[int, int]]:
    if is_horizontal_line(point_1, point_2):
        if point_2[0] > point_1[0]:
            return point_1, point_2
        return point_2, point_1
    if point_2[1] > point_1[1]:
        return point_1, point_2
    return point_2, point_1


def get_line_length(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> int:
    if is_horizontal_line(point_1, point_2):
        return point_2[0] - point_1[0] + 1
    return point_2[1] - point_1[1] + 1


def add_sand_starting_point(scan: List[List[str]], min_x: int) -> None:
    scan[0][500 - min_x + 1] = '+'


def pour_sand(scan: List[List[str]], min_x: int) -> None:
    sand_x = 500 - min_x + 1
    sand_y = 0
    while True:
        if scan[sand_y + 1][sand_x] not in ('x', 'o'):
            sand_y += 1
            continue

        if scan[sand_y + 1][sand_x - 1] not in ('x', 'o'):
            sand_y += 1
            sand_x -= 1
            continue

        if scan[sand_y + 1][sand_x + 1] not in ('x', 'o'):
            sand_y += 1
            sand_x += 1
            continue

        if sand_y == 0:
            raise RuntimeError
        scan[sand_y][sand_x] = 'o'
        break


def main():
    rocks = initialize_rocks()
    min_x, min_y, max_x, max_y = get_rocks_min_max_indices(rocks)
    normalize_rocks(rocks, min_x)

    14.1
    scan = initialize_scan_map(min_x, max_x, max_y)
    add_rocks_to_scan(scan, rocks)
    add_sand_starting_point(scan, min_x)
    try:
        i = 0
        while True:
            pour_sand(scan, min_x)
            i += 1
    except IndexError:
        print(i)

    # 14.2
    scan = initialize_scan_map(min_x, max_x, max_y)
    add_rocks_to_scan(scan, rocks)
    add_sand_starting_point(scan, min_x)
    extend_scan(scan, margin=500)
    min_x = min_x - 500
    add_rock_floor(scan)
    i = 0
    try:
        while True:
            pour_sand(scan, min_x)
            i += 1
    except RuntimeError:
        print(i + 1)

    for line in scan:
        print(''.join(line))


if __name__ == '__main__':
    main()
