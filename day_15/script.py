import numpy as np
import re


def manhatan(a, b):
    return abs(b[1] - a[1]) + abs(b[0] - a[0])


pattern = "[a-z]=-?\d+"


class Info:
    def __init__(self, s, b) -> None:
        self.s = s
        self.b = b
        self.man = manhatan(b, s)
    
    # + man since for ensuring non possible positions we can go beyond element coordinate
    @property
    def max_x(self):
        return max(self.s[0] + self.man, self.b[0])
    @property 
    def min_x(self):
        return min(self.s[0] - self.man , self.b[0])


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
        # Inneficient I am iterating coordinates 
        beacons = set((i.b for i in infos))
        sensors = set((i.s for i in infos))
        width_start, width_end = min([info.min_x for info in infos]), max(
            [info.max_x for info in infos]
        )
        cnt = 0
        ROW = 2000000
        for i in range(width_start, width_end+1):
            if (i,ROW) in beacons or (i,ROW) in sensors:
                continue
            for info in infos:
                if manhatan((i, ROW),info.s) <= info.man:
                    cnt +=1
                    break
        print("COUNT", cnt)
    part_1()
