import select
from time import time
from threading import Thread


def slow_systemcall():
    select.select([], [], [], 0.1)


def run_single_thread():
    start = time()
    for _ in range(5):
        slow_systemcall()
    end = time()
    print('Tooks %.2f seconds for single thread' % (end - start))


def run_multi_thread():
    start = time()
    threads = []
    for _ in range(3):
        thread = Thread(target=slow_systemcall)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    end = time()
    print('Tooks %.2f seconds for multi thread' % (end - start))


if __name__ == '__main__':
    run_single_thread()
    run_multi_thread()