#! /usr/bin/env python
# from pprint import pprint


def sgn(x):
    if x == 0:
        return x
    return x // abs(x)


class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    def pull(self, other):
        if max(abs((x_diff := self.x - other.x)),
               abs((y_diff := self.y - other.y))) == 2:
            other.x += sgn(x_diff)
            other.y += sgn(y_diff)

    def __repr__(self):
        return f"Knot({self.x}, {self.y})"


class LongRope:
    def __init__(self, size):
        self.size = size
        self.knots = [Knot() for _ in range(self.size)]
        self.head = self.knots[0]
        self.tail = self.knots[-1]
        self.tail_pos = {(0, 0)}

    def move(self, dxn, size):
        for _ in range(size):
            if dxn == 'R':
                self.head.x += 1
            elif dxn == 'L':
                self.head.x -= 1
            elif dxn == 'U':
                self.head.y += 1
            elif dxn == 'D':
                self.head.y -= 1

            for i in range(self.size - 1):
                self.knots[i].pull(self.knots[i+1])

            self.tail_pos.add((self.tail.x, self.tail.y))
        # pprint(self.knots)

    def count_tail_pos(self):
        return len(self.tail_pos)


def main():
    rope1 = LongRope(size=2)
    rope2 = LongRope(size=10)
    with open('day9.txt', 'r') as f:
        for line in f:
            # print('=====')
            dxn, sz = line.strip('\n').split(' ')
            # print(f'DXN: {dxn}, SIZ: {sz}')
            rope1.move(dxn, int(sz))
            rope2.move(dxn, int(sz))
    print(f"Part 1: {rope1.count_tail_pos()}")
    print(f"Part 2: {rope2.count_tail_pos()}")


if __name__ == "__main__":
    main()
