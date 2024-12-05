# part 1

from functools import partial, reduce
from itertools import pairwise, starmap
from operator import gt, lt
from sys import stdin

def compose(*fs):
    compose2 = lambda f, g: lambda *args: f(g(*args))
    return reduce(compose2, fs)

def parse():
    return [list(map(int, line.split())) for line in stdin]

def solve(xs):
    is_increasing = compose(all, partial(starmap, lt), pairwise)
    is_decreasing = compose(all, partial(starmap, gt), pairwise)
    is_monotone = lambda xs: is_increasing(xs) or is_decreasing(xs)
    is_not_too_different = compose(
        all,
        partial(starmap, lambda x, y: 1 <= abs(x - y) <= 3),
        pairwise)
    is_safe = lambda xs: is_monotone(xs) and is_not_too_different(xs)
    return sum(map(is_safe, xs))

if __name__ == '__main__':
    print(solve(parse()))