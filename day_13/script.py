from collections import defaultdict
from json import loads
from itertools import zip_longest


def make_same(a, b):
    if type(a) != type(b):
        if type(a) == int:
            a = [a]
        if type(b) == int:
            b = [b]
    return a, b


def rule(a, b, idx):
    if a == b:
        return (False, False)
    if a is None:
        return (True, idx)
    if b is None:
        return (True, 0)
    a, b = make_same(a, b)
    if type(a) == int:
        if a < b:
            return (True, idx)
        if a > b:
            return (True, 0)
    if type(a) == list:
        iter_ = zip_longest(a, b, fillvalue=None)
        c, d = next(iter_)
        done = False
        while not done:
            done, add = rule(c, d, idx)
            if done:
                return done, add
            try:
                c, d = next(iter_)
            except StopIteration:
                return False, False
    # return (False,False)


def part_1(pairs):
    res = 0
    for idx, pair in enumerate(pairs):
        for a, b in zip_longest(pair[0], pair[1], fillvalue=None):
            pair_analysis_done, add = rule(a, b, idx + 1)
            if pair_analysis_done:
                res += add
                break
    return res


def part_2(pairs):
    all_lines = [i for pair in pairs for i in pair]
    all_lines.append([[2]])
    all_lines.append([[6]])
    is_higher_than = defaultdict(int)
    for idx, line in enumerate(all_lines):
        for idx2, line2 in enumerate(all_lines):
            if idx == idx2:
                continue
            for a, b in zip_longest(line, line2, fillvalue=None):
                pair_analysis_done, add = rule(a, b, 10)
                if pair_analysis_done:
                    if add == 0:
                        is_higher_than[str(line)] += 1
                    break

    return ((is_higher_than["[[2]]"] +1) * (1+is_higher_than["[[6]]"]))


with open("input.txt") as f:
    pairs = []
    pair = []
    for line in f.readlines():
        if line.split():
            pair.append(loads(line))
        else:
            if pair:
                pairs.append(pair)
            pair = []
    pairs.append(pair)
    print(part_1(pairs))
    print(part_2(pairs))
