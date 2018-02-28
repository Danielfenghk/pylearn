from collections import deque, OrderedDict
from heapq import heappush, heappop, nsmallest
from bisect import bisect_left

fifo = deque()
fifo.append(5)
fifo.popleft()

a = OrderedDict()
a['foo'] = 1
a['bar'] = 2

b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for k, v in zip(a.values(), b.values()):
    print(k, v)


a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 1)
heappush(a, 10)
print(nsmallest(2, a))

n = list(range(10**6))
print(bisect_left(n, -1))