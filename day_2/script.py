always_get = {"X": 1, "Y": 2, "Z": 3}
mappings = {"A": "X", "B": "Y", "C": "Z"}
loose_mappings = {"A": "Z", "B": "X", "C": "Y"}
win_mappings = {"A": "Y", "B": "Z", "C": "X"}


def find_strategy(a, b):
    if b == "Y":
        return mappings[a]
    if b == "X":
        return loose_mappings[a]
    if b == "Z":
        return win_mappings[a]


def score(a, b):
    if a == "A":
        if b == "Y":
            return 6
        if b == "Z":
            return 0
    if a == "B":
        if b == "X":
            return 0
        if b == "Z":
            return 6
    if a == "C":
        if b == "X":
            return 6
        if b == "Y":
            return 0


def match_score(opponent_strategy, my_strategy):
    outcome = 0
    if mappings[opponent_strategy] == my_strategy:
        outcome += 3
    else:
        outcome += score(opponent_strategy, my_strategy)

    return outcome + always_get[my_strategy]


with open("input.txt") as f:
    lines = f.readlines()
    total_score = 0
    for line in lines:
        opponent, mine = line.split(" ")
        mine = find_strategy(opponent, mine[0])
        total_score += match_score(opponent, mine[0])
    print(total_score)
