import copy
from dataclasses import dataclass
from pathlib import Path
from typing import List, Callable

puzzle_input = Path('inputs/11').read_text()


@dataclass
class Monkey:
    items: List[int] = None
    operation: str = None
    divisible_by: int = None
    true_monkey: int = None
    false_monkey: int = None
    inspection_count: int = 0


def get_new_worry_level(old: int, operation: str):
    operation = operation.replace('old', str(old))
    return eval(operation)


monkeys: List[Monkey] = []

for line in puzzle_input.splitlines():
    if line.startswith('Monkey'):
        monkey = Monkey()
    elif line.startswith('  Starting items: '):
        items_string = line.split('  Starting items: ')[1]
        monkey.items = [int(item) for item in items_string.split(',')]
    elif line.startswith('  Operation: new = '):
        monkey.operation = line.split('  Operation: new = ')[1]
    elif line.startswith('  Test: divisible by '):
        monkey.divisible_by = int(line.split('  Test: divisible by ')[1])
    elif line.startswith('    If true: throw to monkey '):
        monkey.true_monkey = int(line.split('    If true: throw to monkey ')[1])
    elif line.startswith('    If false: throw to monkey '):
        monkey.false_monkey = int(line.split('    If false: throw to monkey ')[1])
    else:
        monkeys.append(monkey)
monkeys.append(monkey)
monkeys_2 = copy.deepcopy(monkeys)

# 11.1
nr_of_rounds = 20

for _ in range(nr_of_rounds):
    for monkey in monkeys:
        for i, item in enumerate(monkey.items):
            monkey.inspection_count += 1
            monkey.items[i] = get_new_worry_level(old=item, operation=monkey.operation)
            monkey.items[i] = monkey.items[i] // 3
            if monkey.items[i] % monkey.divisible_by:
                monkeys[monkey.false_monkey].items.append(monkey.items[i])
            else:
                monkeys[monkey.true_monkey].items.append(monkey.items[i])
        monkey.items = []

monkeys_sorted_by_inspection_count = sorted(monkeys, key=lambda x: x.inspection_count, reverse=True)
print(monkeys_sorted_by_inspection_count[0].inspection_count * monkeys_sorted_by_inspection_count[1].inspection_count)

# 11.2
nr_of_rounds = 10000

common_denominator = 1
for monkey in monkeys_2:
    common_denominator *= monkey.divisible_by

for i in range(nr_of_rounds):
    for monkey in monkeys_2:
        for i, item in enumerate(monkey.items):
            monkey.inspection_count += 1
            monkey.items[i] = get_new_worry_level(old=item, operation=monkey.operation)
            if monkey.items[i] % monkey.divisible_by:
                monkeys_2[monkey.false_monkey].items.append(monkey.items[i])
            else:
                monkeys_2[monkey.true_monkey].items.append(monkey.items[i])
        monkey.items = []
    for monkey in monkeys_2:
        for i, item in enumerate(monkey.items):
            monkey.items[i] = monkey.items[i] % common_denominator

monkeys_2_sorted_by_inspection_count = sorted(monkeys_2, key=lambda x: x.inspection_count, reverse=True)
print(
    monkeys_2_sorted_by_inspection_count[0].inspection_count * monkeys_2_sorted_by_inspection_count[1].inspection_count)
