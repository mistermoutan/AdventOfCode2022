import numpy as np

def manhattan_distance(a, b):
    return np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])

def are_adjacent(a, b):
    dist = manhattan_distance(a, b)
    if dist <= 1:
        return True
    if dist == 2:
        if a[0] != b[0] and a[1] != b[1]:
            return True
        return False

    return False


def move(pos, direction):
    if direction == "U":
        pos[0] += 1
    elif direction == "D":
        pos[0] -= 1
    elif direction == "R":
        pos[1] += 1
    elif direction == "L":
        pos[1] -= 1
    return pos


def move_tail(tail_pos, head_pos):
    if tail_pos[0] == head_pos[0]:
        if head_pos[1] > tail_pos[1]:
            return move(tail_pos, "R")
        else:
            return move(tail_pos, "L")
    elif tail_pos[1] == head_pos[1]:
        if head_pos[0] > tail_pos[0]:
            return move(tail_pos, "U")
        else:
            return move(tail_pos, "D")
    else:
        x_diff = head_pos[0] - tail_pos[0]
        y_diff = head_pos[1] - tail_pos[1]
        movement = [None, None]
        if x_diff < 0:
            movement[0] = -1
        else:
            movement[0] = 1
        if y_diff < 0:
            movement[1] = -1
        else:
            movement[1] = 1
        tail_pos[0] += movement[0]
        tail_pos[1] += movement[1]
        return tail_pos

with open("input.txt") as f:
    lines = f.readlines()
    knots = {i: [0, 0] for i in range(10)}
    tail_visited = set()
    # last knot is tail, first is head
    tail_visited.add(tuple(knots[len(knots)-1]))
    for idx, line in enumerate(lines):
        line = line.strip("\n")
        direction, n = line.split(" ")
        for _ in range(int(n)):
            knots[0] = move(knots[0], direction)
            for i in range(1,len(knots)):
                if not are_adjacent(knots[i - 1], knots[i]):
                    knots[i] = move_tail(knots[i], knots[i - 1])
                tail_visited.add(tuple(knots[len(knots)-1]))
    print(len(tail_visited))
