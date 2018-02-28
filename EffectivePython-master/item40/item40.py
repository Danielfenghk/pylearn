def my_coroutine():
    while True:
        received = yield
        print('Received:', received)


it = my_coroutine()
next(it)
it.send('hello')
it.send('world')


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(current, value)

it = minimize()
next(it)
print(it.send(10))
print(it.send(5))
print(it.send(30))
print(it.send(-2))
print(it.send(90))