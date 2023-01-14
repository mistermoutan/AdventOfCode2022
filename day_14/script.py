from typing import Counter
import numpy as np


def add_to_grid(grid, rock):
    for idx in range(0, len(rock) - 1, 1):
        try:
            start, finish = rock[idx], rock[idx + 1]
            start_split = start.split(",")
            finish_split = finish.split(",")
            start_x, start_y = int(start_split[1]), int(start_split[0])
            grid[start_x, start_y] = "#"
            finish_x, finish_y = int(finish_split[1]), int(finish_split[0])
            diff_x = finish_x - start_x
            diff_y = finish_y - start_y
        except IndexError:
            break
        for i in range(abs(diff_x)):
            assert diff_y == 0
            if diff_x > 0:
                grid[start_x + i + 1, start_y] = "#"
            else:
                grid[start_x - i - 1, start_y] = "#"
        for i in range(abs(diff_y)):
            assert diff_x == 0
            if diff_y > 0:
                grid[start_x, start_y + i + 1] = "#"
            else:
                grid[start_x, start_y - i - 1] = "#"


def add_floor(grid):
    for i in range(grid.shape[0]):
        if "#" in grid[i]:
            last_rock = i
    for j in range(grid.shape[1]):
        grid[last_rock + 2, j] = "#"


def throw_sand(grid):
    sand_x = 0
    sand_y = 500
    moved = False
    while True:
        # part 2: with floor thre is no index error
        # try:
        if grid[sand_x + 1, sand_y] == ".":
            moved = True
            sand_x = sand_x + 1
        elif grid[sand_x + 1, sand_y - 1] == ".":
            moved = True
            sand_x = sand_x + 1
            sand_y = sand_y - 1
        elif grid[sand_x + 1, sand_y + 1] == ".":
            moved = True
            sand_x = sand_x + 1
            sand_y = sand_y + 1
        else:
            if sand_x == 0 and sand_y == 500:
                return False
            grid[sand_x, sand_y] = "o"
            break
        # except IndexError:
        # return False
    return moved


with open("input.txt") as f:
    lines = f.readlines()
    rock_lines = []
    grid = np.full((1000, 1000), ".")
    for line in lines:
        rock_line = line.strip("\n").split("->")
        rock_lines.append(rock_line)
    for rock in rock_lines:
        add_to_grid(grid, rock)
    add_floor(grid)
    cnt = 0
    while throw_sand(grid) is True:
        cnt += 1
    print(cnt + 1) # + 1 for part 2
