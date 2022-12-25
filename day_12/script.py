import numpy as np

def is_goal(grid, v):
    return grid[v[0], v[1]] == 123

def get_adjacent(grid, v):
    value = grid[v[0], v[1]]
    u, d, r, l = (v[0] - 1, v[1]), (v[0] + 1, v[1]), (v[0], v[1] - 1), (v[0], v[1] + 1)
    res = [u, d, r, l]
    return [
        i
        for i in res
        if not (np.array(i) < 0).any()
        and (i[0] <= grid.shape[0] - 1)
        and (i[1] <= grid.shape[1] - 1)
        and (grid[i[0], i[1]] <= value + 1)
    ]

class Node:
    def __init__(self, coords, depth):
        self.coords = coords
        self.depth = depth

def bfs(grid, root):
    root = Node(root, 0)
    Q = [root]
    explored = {tuple(root.coords)}
    while Q:
        v = Q.pop(0)
        if is_goal(grid, v.coords):
            return v.depth
        candidates = get_adjacent(grid, v.coords)
        for c in candidates:
            if tuple(c) not in explored:
                explored.add(tuple(c))
                Q.append(Node(c, v.depth + 1))
    return 1000000


with open("input.txt") as f:
    grid = []
    lines = f.readlines()
    for idx, line in enumerate(lines):
        line = line.strip("\n")
        grid.append([ord(i) for i in line])
    grid = np.array(grid)
    # handle start and end coordinates
    S = np.argwhere(grid == 83)
    x_s, y_s = S[0, 0], S[0, 1]
    grid[x_s, y_s] += 13
    E = np.argwhere(grid == 69)
    x_e, y_e = E[0, 0], E[0, 1]
    grid[x_e, y_e] += 54
    starts = np.argwhere(grid == 97)
    distances = []
    for start in starts:
        distances.append(bfs(grid,[start[0],start[1]]))
    print(sorted(distances)[0])
