#! /usr/bin/env python

def parse_cal_file():
    cal_counts = [0]
    with open('day1.txt', 'r') as f:
        for line in f:
            if line == '\n':
                cal_counts.append(0)
            else:
                cal_counts[-1] += int(line)
    return cal_counts


def main():
    cals = parse_cal_file()
    sorted_cals = sorted(cals, reverse=True)
    print(f"Part one: {sorted_cals[0]}")
    print(f"Part two: {sum(sorted_cals[:3])}")


if __name__ == '__main__':
    main()
