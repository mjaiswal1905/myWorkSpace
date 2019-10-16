def fib_gen():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x+y

fs = fib_gen()

print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))