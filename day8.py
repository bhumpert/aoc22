#! /usr/bin/env python
from dataclasses import dataclass
from functools import reduce


@dataclass
class Grid:
    data: list[list[int]]

    def get_row(self, ix: int) -> list[int]:
        return self.data[ix]

    def get_col(self, ix: int) -> list[int]:
        return [row[ix] for row in self.data]

    @property
    def num_rows(self):
        return len(self.data)

    @property
    def num_cols(self):
        return len(self.data[0])


def visible_ixs(series: list[int], limit=10):
    vis = []
    high = -1
    for ix, val in enumerate(series):
        if val > high:
            high = val
            vis.append(ix)
            if val >= limit:
                break
    return vis


def find_visible_count(grid: Grid) -> int:
    visible: set[tuple[int, int]] = set()
    m = grid.num_rows
    n = grid.num_cols
    for i in range(m):
        fwd_vis = visible_ixs(grid.get_row(i))
        bwd_vis = visible_ixs(grid.get_row(i)[::-1])
        for j in fwd_vis:
            visible.add((i, j))
        for j in bwd_vis:
            visible.add((i, n - j - 1))

    for j in range(n):
        fwd_vis = visible_ixs(grid.get_col(j))
        bwd_vis = visible_ixs(grid.get_col(j)[::-1])
        for i in fwd_vis:
            visible.add((i, j))
        for i in bwd_vis:
            visible.add((m - i - 1, j))

    return len(visible)


def zipper(seq):
    left = []
    right = seq
    while right:
        val, *right = right
        yield left, val, right
        left.append(val)


def find_most_scenic(grid: Grid) -> int:
    m = grid.num_rows
    n = grid.num_cols
    raw_scores: dict[tuple[int, int], list[int]] = {(i, j): [] for i in
                                                    range(m) for j in range(n)}

    def trunc_limit(seq, lim):
        for x in seq:
            yield x
            if x >= lim:
                break

    for i in range(m):
        row = grid.get_row(i)
        for j, (left, val, right) in enumerate(zipper(row)):
            raw_scores[(i, j)].append(len(list(trunc_limit(left[::-1], val))))
            raw_scores[(i, j)].append(len(list(trunc_limit(right, val))))

    for j in range(n):
        col = grid.get_col(j)
        for i, (left, val, right) in enumerate(zipper(col)):
            raw_scores[(i, j)].append(len(list(trunc_limit(left[::-1], val))))
            raw_scores[(i, j)].append(len(list(trunc_limit(right, val))))

    scores = []
    for score_list in raw_scores.values():
        scores.append(reduce(lambda x, y: x * y, score_list, 1))

    return max(scores)


def parse_grid() -> Grid:
    data = []
    with open('day8.txt', 'r') as f:
        for line in f:
            data.append(list(map(int, line.strip())))
    return Grid(data=data)


def main():
    grid = parse_grid()
    print(f"Part 1: {find_visible_count(grid)}")
    print(f"Part 2: {find_most_scenic(grid)}")


if __name__ == "__main__":
    main()
