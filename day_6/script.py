with open("input.txt") as f:
    lines = f.readlines()
    succession = 0
    for line in lines:
        for idx, char in enumerate(line):
            sliding_window = line[idx:idx+14]
            if len(set(sliding_window)) == 14:
                print(idx+14)
                exit()

