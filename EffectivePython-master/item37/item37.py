from time import time
from threading import Thread


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


class FactThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


if __name__ == '__main__':
    start = time()
    numbers = [21938, 398540, 203904, 404303, 22234432]
    threads = []
    for n in numbers:
        thread = FactThread(n)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end = time()
    print('Took %.3f seconds' % (end - start))