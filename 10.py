from dataclasses import dataclass
from pathlib import Path

puzzle_input = Path('inputs/10').read_text()

X = 1
cycles_history = []


@dataclass
class Command:
    cycles: int
    value: int


commands = []

for command in puzzle_input.splitlines():
    if command == 'noop':
        commands.append(Command(cycles=1, value=0))
    else:
        commands.append(Command(cycles=2, value=int(command.split()[1])))

for command in commands:
    for _ in range(command.cycles):
        cycles_history.append(X)
    X += command.value


def calculate_signal_strength(cycle_number):
    return cycles_history[cycle_number - 1] * cycle_number

# 10.1

strength_20 = calculate_signal_strength(20)
strength_60 = calculate_signal_strength(60)
strength_100 = calculate_signal_strength(100)
strength_140 = calculate_signal_strength(140)
strength_180 = calculate_signal_strength(180)
strength_220 = calculate_signal_strength(220)

print(strength_20 + strength_60 + strength_100 + strength_140 + strength_180 + strength_220)

# 10.2

crt_line = ''
for i, register_value in enumerate(cycles_history):
    if register_value - 1 <= i % 40 <= register_value + 1:
        crt_line += '#'
    else:
        crt_line += '.'
    if (i + 1) % 40 == 0:
        print(crt_line)
        crt_line = ''
