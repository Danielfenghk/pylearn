def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    results = []
    total = sum(numbers)
    for visit in numbers:
        percent = 100 * visit / total
        results.append(percent)
    return results


class ReadVisits(object):

    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


if __name__ == '__main__':
    DATA_PATH = 'visits.txt'
    it = ReadVisits(DATA_PATH)
    print(normalize_defensive(it))
    