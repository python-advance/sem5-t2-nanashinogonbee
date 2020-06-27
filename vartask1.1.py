import itertools

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

num = 10
print(', '.join(str(i) for i in itertools.islice(fib(), num)))

