#! /usr/bin/env python

def score_line_part1(line):
    mapping = {'X': 0, 'Y': 1, 'Z': 2, 'A': 0, 'B': 1, 'C': 2}
    def enum(c): return mapping[c]
    them, me = map(enum, line.split())
    score = 1 + me + 3 * ((me - them + 1) % 3)
    return score


def score_line_part2(line):
    mapping = {'X': 0, 'Y': 1, 'Z': 2, 'A': 0, 'B': 1, 'C': 2}
    def enum(c): return mapping[c]
    them, res = map(enum, line.split())
    score = 1 + (res + them - 1) % 3 + 3 * res
    return score


def main():
    score_part1 = 0
    score_part2 = 0
    with open('day2.txt', 'r') as f:
        for line in f:
            score_part1 += score_line_part1(line)
            score_part2 += score_line_part2(line)
    print(f"part one: {score_part1}")
    print(f"part two: {score_part2}")


if __name__ == '__main__':
    main()
