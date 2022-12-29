import functools
from pathlib import Path
from typing import List, Tuple

puzzle_input = Path('inputs/13').read_text().splitlines()


def compare_left_and_right_elements(left_elem: int | List, right_elem: int | List) -> int:
    if isinstance(left_elem, int) and isinstance(right_elem, int):
        if left_elem > right_elem:
            return 1
        if left_elem < right_elem:
            return -1
        return 0
    if isinstance(left_elem, int) and isinstance(right_elem, list):
        left_elem = [left_elem]
    elif isinstance(left_elem, list) and isinstance(right_elem, int):
        right_elem = [right_elem]
    return compare_packet_lists(left_packet=left_elem, right_packet=right_elem)


def compare_packet_pair(packet_pair: Tuple[List, List]) -> bool:
    left_packet, right_packet = packet_pair
    return compare_packet_lists(left_packet, right_packet)


def compare_packet_lists(left_packet: List, right_packet: List) -> int:
    while True:
        if len(left_packet) == 0 and len(right_packet) == 0:
            return 0
        if len(left_packet) == 0:
            return -1
        if len(right_packet) == 0:
            return 1
        left_elem = left_packet[0]
        right_elem = right_packet[0]

        result = compare_left_and_right_elements(left_elem, right_elem)
        if result == 0:
            left_packet = left_packet[1:]
            right_packet = right_packet[1:]
            continue
        return result


def initialize_packet_pairs() -> List[Tuple[List, List]]:
    packet_pairs: List[Tuple[List, List]] = []
    for i in range(0, len(puzzle_input), 3):
        packet_pair = (eval(puzzle_input[i]), eval(puzzle_input[i + 1]))
        packet_pairs.append(packet_pair)
    return packet_pairs


def initialize_packets() -> List[List]:
    packets: List[List] = []
    for i in range(0, len(puzzle_input), 3):
        packets.append(eval(puzzle_input[i]))
        packets.append(eval(puzzle_input[i + 1]))
    packets.append([[2]])
    packets.append([[6]])
    return packets


# 13.1
packet_pairs = initialize_packet_pairs()
right_order_indexes = []
wrong_order_indexes = []
for i, packet_pair in enumerate(packet_pairs):
    result = compare_packet_pair(packet_pair)
    if result == -1:
        right_order_indexes.append(i + 1)
    else:
        wrong_order_indexes.append(i + 1)
print(sum(right_order_indexes))

# 13.2
packets = initialize_packets()
packets.sort(key=functools.cmp_to_key(compare_packet_lists))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
