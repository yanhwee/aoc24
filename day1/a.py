# part 1

from operator import sub
from sys import stdin

def parse():
    return (map(int, line.split()) for line in stdin)

def solve(xs):
    return sum(map(abs, map(sub, *map(sorted, zip(*xs)))))

if __name__ == '__main__':
    print(solve(parse()))