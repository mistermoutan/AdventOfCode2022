from json import loads
from itertools import zip_longest


def make_same(a, b):
    if type(a) != type(b):
        if type(a) == int:
            a = [a]
        if type(b) == int:
            b = [b]
    return a,b


def rule(a, b, idx):
    print(f"a {a}, b {b}")
    if a == b: 
        return (False,False)
    if a is None:
         return (True,idx)
    if b is None:
        return (True,0)
    a,b = make_same(a, b)
    print(f"After same {a}, {b}")
    if type(a) == int:
        if a < b:
            return (True,idx)
        if a > b:
            return (True,0)
    if type(a) == list:
        iter_ = zip_longest(a, b, fillvalue=None)
        c,d = next(iter_)
        done = False
        while not done:
            done, add = rule(c,d,idx)
            if done:
                return done, add
            try:
                c,d = next(iter_)
            except StopIteration:
                return False,False

def part_1(pairs):
    res = 0
    for idx, pair in enumerate(pairs):
        for a, b in zip_longest(pair[0], pair[1], fillvalue=None):
            print(f"\n PAIRS: \n {pair[0]} \n {pair[1]}")
            pair_analysis_done, add = rule(a, b, idx+1)
            if pair_analysis_done:
                res += add
                break
    return res



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
