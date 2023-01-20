from collections import defaultdict
import re


def manhatan(a, b):
    return abs(b[1] - a[1]) + abs(b[0] - a[0])


pattern = "[a-z]=-?\d+"


class Info:
    def __init__(self, s, b) -> None:
        self.s = s
        self.b = b
        self.man = manhatan(b, s)

    # properties for part 1
    # + man since for ensuring non possible positions we can go beyond element coordinate
    @property
    def max_x(self):
        return max(self.s[0] + self.man, self.b[0])

    @property
    def min_x(self):
        return min(self.s[0] - self.man, self.b[0])


def get_perimeter_elems(info):
    """get_perimeter_elems.
    get all points immediately outside the boundary where a beacon can not possible be located given a sensor positon
    and the manhatan distance to its closest beacon
    :param info:
    """
    x, y = info.s[0], info.s[1]
    res = set()
    for idx, i in enumerate(range(x, x + info.man + 2)):
        if (
            not (0 < i < 4000000)
            or not (0 < y + info.man + 1 - idx < 4000000)
            or not (0 < y - info.man - 1 + idx < 4000000)
        ):
            continue
        res.add((i, y + info.man + 1 - idx))
        res.add((i, y - info.man - 1 + idx))
    for idx, i in enumerate(reversed(range(x - info.man - 2, x))):
        if (
            not (0 < i < 4000000)
            or not (0 < y + info.man + 1 - idx < 4000000)
            or not (0 < y - info.man - 1 + idx < 4000000)
        ):
            continue
        res.add((i, y + info.man + 1 - idx))
        res.add((i, y - info.man - 1 + idx))
    print(len(res))
    return res


with open("input.txt") as f:
    lines = f.readlines()
    infos = []
    for line in lines:
        matches = re.findall(pattern, line)
        x_s, y_s, x_b, y_b = (
            int(matches[0].split("=")[1]),
            int(matches[1].split("=")[1]),
            int(matches[2].split("=")[1]),
            int(matches[3].split("=")[1]),
        )
        infos.append(Info((x_s, y_s), (x_b, y_b)))

    def part_1():
        # Inneficient as I am just iterating over all coordinates in row
        beacons = set((i.b for i in infos))
        sensors = set((i.s for i in infos))
        width_start, width_end = min([info.min_x for info in infos]), max(
            [info.max_x for info in infos]
        )
        cnt = 0
        ROW = 2000000
        for i in range(width_start, width_end + 1):
            if (i, ROW) in beacons or (i, ROW) in sensors:
                continue
            for info in infos:
                if manhatan((i, ROW), info.s) <= info.man:
                    cnt += 1
                    break
        print("COUNT", cnt)

    def part_2():
        """part_2.
        Rationale: the beacon will have to be located immediately outside a boundary (be a perimeter
        element). Furthermore, it will have to be a perimeter element to at least 2 sensors.
        This takes ~30s in Python so definetely a lot of room for improvement.
        Great solutions using line intersection (wish I had though of that):
        - https://www.reddit.com/r/adventofcode/comments/zmcn64/comment/j0b90nr/?context=3
        - https://github.com/BuonHobo/advent-of-code/blob/master/2022/15/Alex/second.py
        """
        def is_goal(pt, infos):
            for info in infos:
                if manhatan(pt, info.s) <= info.man:
                    return False
            return True

        occurences = defaultdict(int)
        checked = set()
        for info in infos:
            perimeter_points = get_perimeter_elems(info)
            for pt in perimeter_points:
                if pt in checked:
                    continue
                occurences[pt] += 1
                if occurences[pt] > 1:
                    if is_goal(pt, infos):
                        print(pt[0] * 4000000 + pt[1])
                    else:
                        checked.add(pt)

    part_2()
