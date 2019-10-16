'''
f0 - 0
f1 - 1
f2 - f1+f0
f3 - f2+f1
f4 - f3+f2
'''


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    for iteration in range(10):
        print(fibonacci(iteration))