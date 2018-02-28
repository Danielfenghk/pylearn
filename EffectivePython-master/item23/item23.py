from collections import defaultdict


class CountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = CountMissing()

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 10),
    ('orange', 9)
]

result = defaultdict(counter, current)
for k, v in increments:
    result[k] += v
assert counter.added == 2

