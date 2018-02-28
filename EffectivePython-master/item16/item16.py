def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield 0
        for letter in line:
            offset += 1
            if letter is ' ':
                yield offset


if __name__ == '__main__':
    from itertools import islice
    with open('file.txt') as f:
        it = index_file(f)
        # print(list(it))
        results = islice(it, 0, 3)
        print(list(results))