def fibonacci(n):
    x, y = 0, 1
    if n == 0:
        return 0
    for _ in range(n-1):
        x, y = y, x+y

    return y

if __name__ == '__main__':
    for iteration in range(10):
        print(fibonacci(iteration))