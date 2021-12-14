from aoc import *


def part1(data):
    horizontal, depth = 0, 0
    for c in data:
        direction, step = c.split(' ')
        if direction == 'forward':
            horizontal += int(step)
        elif direction == 'up':
            depth -= int(step)
        else:  # down
            depth += int(step)
    return horizontal * depth


def part2(data):
    horizontal, depth, aim, = 0, 0, 0
    for c in data:
        direction, step = c.split(' ')
        if direction == 'forward':
            horizontal += int(step)
            depth += aim * int(step)
        elif direction == 'up':
            aim -= int(step)
        else:  # down
            aim += int(step)
    return horizontal * depth


data = read_input(2)
print(data)

print(part1(data))
print(part2(data))
