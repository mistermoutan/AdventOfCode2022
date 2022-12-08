import string

def parse(line):
    a,b = line.split(",")
    min_a,max_a = a.split("-")
    min_a,max_a = int(min_a),int(max_a)
    min_b,max_b = b.split("-")
    min_b,max_b = int(min_b),int(max_b)
    return min_a,max_a,min_b,max_b

def contains(min_a,max_a,min_b,max_b):

    if min_a >= min_b and max_a <= max_b:
        return True
    if min_b >= min_a and max_b <= max_a:
        return True
    return False

def overlaps(min_a,max_a,min_b,max_b):
    range_a = max_a - min_a
    range_b = max_b - min_b
    if (min_a + range_a) >= min_b and (min_a + range_a) <= max_b:
        return True
    if (min_b + range_b) >= min_a and (min_b + range_b) <= max_a:
        return True
    return False


with open("input.txt") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        line = line.strip("\n")
        a,b,c,d = parse(line)
        if overlaps(a,b,c,d):
            total +=1
    print(total)
