memory = {0: 0, 1: 1}


def fibonacci(n):
    if n not in memory:
        memory[n] = fibonacci(n-1) + fibonacci(n-2)

    return memory[n]

if __name__ == '__main__':
    for iteration in range(10):
        print(fibonacci(iteration))