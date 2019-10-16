def factorial(n):
    result = 1
    for iteration in range(2, n+1):
        result = result * iteration

    print(result)


factorial(5)