import string


def unique_compartments_inventory(line):
    a, b = set(), set()
    total_items = len(line)
    items_per_compartment = total_items / 2
    for idx, i in enumerate(line):
        if idx < items_per_compartment:
            a.add(i)
        else:
            b.add(i)
    return a, b


def item_priority(a):
    return ord(a) - 96 if a.islower() else ord(a) - 38


with open("input.txt") as f:
    lines = f.readlines()
    total = 0
    buffer = []
    for line in lines:
        line = line.strip("\n")
        buffer.append(set(line))
        if len(buffer) == 3:
            intersect = set.intersection(*buffer)
            buffer.clear()
            total += item_priority(intersect.pop())

    print(total)
