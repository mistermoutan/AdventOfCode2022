from collections import defaultdict
from typing import Dict, List, NamedTuple


class DirElement:
    def __init__(self, type_, file_size, name):
        self.type = type_
        self.name = name
        self.size = file_size


dirs_to_content: Dict[str, List[DirElement]] = defaultdict(list)

base_dir = DirElement("dir", "-", "/")
base_dir.parent = False


def is_command(line):
    return True if line[0] == "$" else False


def parse_command(line, current_dir) -> DirElement:
    split = line.split(" ")
    if "ls" == split[1]:
        return current_dir
    if "cd" == split[1]:
        if split[2] == "..":
            # return get_parent_directory(current_dir)
            return current_dir.parent
        if split[2] == "/":
            return base_dir
        # if element has already been checked
        if dirs_to_content.get(id(current_dir), None) is not None:
            for element in dirs_to_content[id(current_dir)]:
                if element.name == split[2]:
                    return element
        # if not create new
        res = DirElement("dir", split[2], "-")
        res.parent = current_dir
        return res


def parse_out(line, current_dir):
    split = line.split(" ")
    if split[0] == "dir":
        new_element = DirElement("dir", 0, split[1])
        new_element.parent = current_dir
        dirs_to_content[id(current_dir)].append(new_element)
    else:
        dirs_to_content[id(current_dir)].append(DirElement("file", int(split[0]), split[1]))


def get_size_of_dir(dir_id):
    total = 0
    for element in dirs_to_content[dir_id]:
        if element.type == "file":
            total += element.size
        else:
            total += get_size_of_dir(id(element))
    return total


def get_used_space():
    return get_size_of_dir(id(base_dir))


def get_directories_of_max_size(x: int):
    total_of_all = 0
    for dir_id in dirs_to_content.keys():
        total = get_size_of_dir(dir_id)
        if total <= x:
            total_of_all += total
    return total_of_all


def get_smallest_directory_above(x):
    candidates = []
    for dir_id in dirs_to_content.keys():
        total = get_size_of_dir(dir_id)
        if total >= x:
            candidates.append(total)
    return sorted(candidates)


with open("input.txt") as f:
    lines = f.readlines()
    current_dir = None
    for idx, line in enumerate(lines):
        # right now assuming mapping come from ls only
        line = line.strip("\n")
        if is_command(line):
            current_dir = parse_command(line, current_dir)
        else:
            parse_out(line, current_dir)

    print(get_directories_of_max_size(100000))
    space_left = 70000000 - get_used_space()
    print(get_used_space(),space_left)
    print(get_smallest_directory_above(30000000 - space_left))
