# part 2

from collections import Counter

from a import parse

def solve(xs):
    xs, ys = zip(*xs)
    xs, ys = Counter(xs), Counter(ys)
    return sum(k * c * ys[k] for k, c in xs.items())

if __name__ == '__main__':
    print(solve(parse()))