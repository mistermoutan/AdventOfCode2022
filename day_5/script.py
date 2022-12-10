from queue import LifoQueue


containers = [[] for _ in range(9)]

with open("input.txt") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        if line[0] == "[":
            for idx, char in enumerate(line):
                if char == "[":
                    containers[idx // 4].append(line[idx + 1])
        line = line.strip("\n")
        if line and line[0]=="m":
            split = line.split(" ")
            print(line,split)
            quantity, from_, to = int(split[1]), int(split[3]), int(split[5])
            to_move = [containers[from_-1].pop(0) for _ in range(quantity)]
            for box in reversed(to_move):
                containers[to-1].insert(0,box)


    print(total)
    for i in containers:
        print(i)
