class Monkey:
    def __init__(self, items, operation, num, test, true_monkey, false_monkey) -> None:
        self.items = items
        self.operation = operation
        self.num = num
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_count = 0

    def __str__(self) -> str:
        return f"items: {self.items} \n operation: {self.operation} \n num: {self.num} \n test: {self.test} \n t_m: {self.true_monkey} \n  f_m: {self.false_monkey} \n inspect_count: {self.inspect_count}"

    def get_item(self, s):
        self.inspect_count += 1
        return op(self.items.pop(0), self.operation, self.num) % s

    def do_test(self, item):
        return item % self.test == 0


def op(x, operator, num_or_str):
    if num_or_str == "old":
        num_or_str = x
    return eval(f"{x} {operator} {num_or_str}")


def make_da_monkey(monkey):
    items = [np.int64(i) for i in (monkey[1].split(":")[1]).split(",")]
    operation, num = monkey[2].split()[-2], monkey[2].split()[-1]
    test = np.int64(monkey[3].split()[-1])
    true_monkey = int(monkey[4].split()[-1])
    false_monkey = int(monkey[5].split()[-1])
    return Monkey(items, operation, num, test, true_monkey, false_monkey)


def do_round(monkeys, s):
    for i in range(len(monkeys)):
        m = monkeys[i]
        while len(m.items) != 0:
            item = m.get_item(s)
            if m.do_test(item):
                monkeys[m.true_monkey].items.append(item)
            else:
                monkeys[m.false_monkey].items.append(item)


def super_mod(monkeys):
    res = 1
    divisors = [m.test for m in monkeys.values()]
    for i in divisors:
        res = res * i
    return res


with open("input.txt") as f:
    monkeys = {
        i: make_da_monkey([next(f).strip("\n") for _ in range(0 + i, 7 + i)]) for i in range(0, 8)
    }
    s = super_mod(monkeys)
    for _ in range(10000):
        do_round(monkeys, s)
    c = sorted([m.inspect_count for m in monkeys.values()])
    print(c[-1] * c[-2])
