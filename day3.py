#! /usr/bin/env python

from itertools import islice


def character_to_number(char):
    if 97 <= ord(char) <= 122:
        return ord(char) - 96
    if 65 <= ord(char) <= 90:
        return ord(char) - 64 + 26
    raise Exception


def part1_scoreline(line):
    assert len(line) % 2 == 0

    n = len(line) // 2
    first_set = set(line[:n])
    second_set = set(line[n:])

    inter = first_set.intersection(second_set)

    assert len(inter) == 1

    return character_to_number(inter.pop())


def part2_scorelines(lines):
    set1, set2, set3 = map(set, lines)
    inter = set1.intersection(set2).intersection(set3)
    assert len(inter) == 1
    return character_to_number(inter.pop())


def chunks(seq, n):
    iterator = iter(seq)
    for item in iter(lambda: list(islice(iterator, n)), []):
        yield item


def main():
    part1_score = 0
    part2_score = 0
    with open('day3.txt', 'r') as f:
        for line in f:
            part1_score += part1_scoreline(line.strip())
    with open('day3.txt', 'r') as f:
        for lines in chunks(f, 3):
            stripped_lines = [line.strip() for line in lines]
            part2_score += part2_scorelines(stripped_lines)
    print(f"Part 1 Score: {part1_score}")
    print(f"Part 2 Score: {part2_score}")


if __name__ == '__main__':
    main()
