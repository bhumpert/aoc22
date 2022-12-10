#! /usr/bin/env python
from itertools import tee


def window(iterable, size):
    iters = tee(iterable, size)
    for i in range(1, size):
        for each in iters[i:]:
            next(each, None)
    return zip(*iters)


def distincts_ix(s, n):
    for i, win in enumerate(window(s, n)):
        if len(set(win)) == n:
            return i + n


def main():
    with open("day6.txt") as f:
        s = f.read().strip('\n')

    print(f"Part 1: {distincts_ix(s, 4)}")
    print(f"Part 2: {distincts_ix(s, 14)}")


if __name__ == "__main__":
    main()
