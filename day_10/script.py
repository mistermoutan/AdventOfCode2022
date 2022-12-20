def part_1(cycles_to_x):
    res = 0
    cycles = [20, 60, 100, 140, 180, 220]
    for i in cycles:
        res += i * cycles_to_x[i]
    return res


def part_2(cycles_to_x):
    crt = [[] for _ in range(240)]
    for cycle, x in cycles_to_x.items():
        # x is pos of middle of sprite (lenght 3), cycle is register pos 0-39 per line. Cycle n draws pos n-1
        if (
            (x == (cycle - 1) % 40)
            or (x == ((cycle - 1) % 40) - 1)
            or (x == ((cycle - 1) % 40) + 1)
        ):
            crt[cycle - 1] = "#"
        else:
            crt[cycle - 1] = "."

    for i in range(0, 240, 40):
        print("".join(i for i in crt[i : i + 39]))


with open("input.txt") as f:
    lines = f.readlines()
    cycle = 0
    X = 1
    cycles_to_x = {}
    for _, line in enumerate(lines):
        line = line.strip("\n").split(" ")
        for _ in range(len(line)):
            cycle += 1
            cycles_to_x[cycle] = X
        try:
            X += int(line[1])
        except IndexError:
            pass
    print(part_1(cycles_to_x))
    print(part_2(cycles_to_x))
