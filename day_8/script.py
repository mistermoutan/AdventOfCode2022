import numpy as np


def is_visible(grid, index, x):
    if (
        np.all(x > grid[index[0], index[1] + 1 :])
        or np.all(x > grid[index[0], : index[1]])
        or np.all(x > grid[: index[0], index[1]])
        or np.all(x > grid[index[0] + 1 :, index[1]])
    ):
        return True
    return False


def scenic_score(grid, index, x):
    a, b, c, d = 0, 0, 0, 0
    for i in grid[index[0], index[1] + 1 :]:
        a += 1
        if x <= i:
            break
    for i in np.flip(grid[index[0], : index[1]]):
        b += 1
        if x <= i:
            break
    for i in np.flip(grid[: index[0], index[1]]):
        c += 1
        if x <= i:
            break
    for i in grid[index[0] + 1 :, index[1]]:
        d += 1
        if x <= i:
            break

    return a * b * c * d


with open("input.txt") as f:
    grid = []
    scenic_scores = []
    lines = f.readlines()
    for idx, line in enumerate(lines):
        line = line.strip("\n")
        grid.append([int(i) for i in line])
    grid = np.array(grid)
    total = 0
    grid_max_idx = grid.shape[0] - 1
    for index, x in np.ndenumerate(grid):
        scenic_scores.append(scenic_score(grid, index, x))
        if grid_max_idx in index or 0 in index:
            total += 1
        else:
            if is_visible(grid, index, x):
                total += 1
    print(total, max(scenic_scores))
