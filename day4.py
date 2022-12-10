#! /usr/bin/env python

def parse_line(line):
    line = line.strip()
    t = tuple(map(lambda x: tuple(map(int, x.split('-'))), line.split(',')))
    return t


def is_fully_overlapped(t):
    t1, t2 = t
    t1, t2 = sorted([t1, t2])

    assert t1[0] <= t2[0]

    return t1[0] == t2[0] or t1[1] >= t2[1]


def is_overlapped(t):
    t1, t2 = t
    t1, t2 = sorted([t1, t2])

    assert t1[0] <= t2[0]

    return t1[1] >= t2[0]


def main():
    part1 = 0
    part2 = 0
    with open("day4.txt", 'r') as f:
        for line in f:
            ass = parse_line(line)
            if is_fully_overlapped(ass):
                part1 += 1
            if is_overlapped(ass):
                part2 += 1
    print(f"Part 1 score: {part1}")
    print(f"Part 2 score: {part2}")


if __name__ == "__main__":
    main()
