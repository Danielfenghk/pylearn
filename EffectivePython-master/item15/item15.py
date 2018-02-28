def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        else:
            return (1, x)
    values.sort(key=helper)


def sort_priority2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        else:
            return (1, x)
    values.sort(key=helper)
    return found


def sort_priority3(values, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        else:
            return (1, x)
    values.sort(key=helper)
    return found


class Sorter:

    def __init__(self, group):
        self.found = False
        self.group = group

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        else:
            return (1, x)


if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    # sort_priority(numbers, group)
    # print(numbers)
    sorter = Sorter(group)
    numbers.sort(key=sorter)
    assert sorter.found is True

    # if sort_priority3(numbers, group):
    #     print('found it.')
    # else:
    #     print("didn't find it. Sorry.")