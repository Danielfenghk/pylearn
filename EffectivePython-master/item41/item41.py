from time import time
from concurrent.futures import ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def run_signal_thread(numbers):
    start = time()
    results = list(map(gcd, numbers))
    print('It takes %.1f seconds' % (time() - start))


def run_thread_pool(numbers):
    pool = ProcessPoolExecutor(max_workers=4)
    start = time()
    results = list(pool.map(gcd, numbers))
    print('It takes %.1f seconds' % (time() - start))


if __name__ == '__main__':
    numbers = [(1293, 2345), (23423, 485982), (93939393, 9393933)]
    run_signal_thread(numbers)
    run_thread_pool(numbers)