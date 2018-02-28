from collections import deque
from threading import Lock, Thread
from time import sleep


class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def get(self):
        with self.lock:
            return self.items.popleft()

    def put(self, item):
        with self.lock:
            self.items.append(item)


class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.poll_count = 0
        self.done_count = 0

    def run(self):
        while True:
            self.poll_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                sleep(0.1)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.done_count += 1


def download(item):
    print('download images')


def resize(item):
    print('resize image')


def upload(item):
    print('upload image')


if __name__ == '__main__':
    download_queue = MyQueue()
    resize_queue = MyQueue()
    upload_queue = MyQueue()
    done_queue = MyQueue()

    threads = [
        Worker(download, download_queue, resize_queue),
        Worker(resize, resize_queue, upload_queue),
        Worker(upload, upload_queue, done_queue)
    ]

    for thread in threads:
        thread.start()

    tasks = 100
    for _ in range(tasks):
        download_queue.put(object())

    while len(done_queue.items) < tasks:
        pass

    processed = len(done_queue.items)
    polled = sum(x.poll_count for x in threads)
    print('Processed', processed, 'items after polling', polled, 'times')

