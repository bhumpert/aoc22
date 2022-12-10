#! /usr/bin/env python
import re
import string

from copy import deepcopy


def parse_input_file():
    with open('day5.txt', 'r') as f:
        schematic_lines = []
        for line in f:
            if line == '\n':
                break
            schematic_lines.append(line.strip('\n'))
        direction_lines = [line.strip('\n') for line in f.readlines()]

    col_pos = {}
    for ix, c in enumerate(schematic_lines[-1]):
        if c in string.digits:
            col_pos[ix] = int(c)
    schematic = [[] for _ in range(len(col_pos))]
    for line in schematic_lines[-2::-1]:
        for ix, c in enumerate(line):
            if c in string.ascii_uppercase:
                schematic[col_pos[ix]-1].append(c)

    directions = []
    for line in direction_lines:
        rx = r"move (?P<qty>\d+) from (?P<src>\d) to (?P<dst>\d)"
        m = re.match(rx, line)
        directions.append(m.groupdict())
    return schematic, directions


def apply_direction_part1(schematic, direction):
    qty = int(direction['qty'])
    src = int(direction['src']) - 1
    dst = int(direction['dst']) - 1
    for _ in range(qty):
        schematic[dst].append(schematic[src].pop())
    return schematic


def apply_direction_part2(schematic, direction):
    qty = int(direction['qty'])
    src = int(direction['src']) - 1
    dst = int(direction['dst']) - 1

    schematic[dst].extend(schematic[src][-qty:])
    schematic[src][-qty:] = []
    return schematic


def top_stuff(schematic):
    return ''.join(map(lambda x: x[-1], schematic))


def main():
    schematic, directions = parse_input_file()
    schematic_part1 = deepcopy(schematic)
    schematic_part2 = deepcopy(schematic)
    for i, direction in enumerate(directions):
        schematic_part1 = apply_direction_part1(schematic_part1, direction)
        schematic_part2 = apply_direction_part2(schematic_part2, direction)
    print(f"Part 1: {top_stuff(schematic_part1)}")
    print(f"Part 2: {top_stuff(schematic_part2)}")


if __name__ == "__main__":
    main()
