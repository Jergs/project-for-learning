num = int(input())
cache = {0: 0, 1: 1}


def fibonacci(n):
    if n in {0, 1}:
        return cache[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = res
    return cache[n]


fibonacci(num)
for inp in range(num):
    print(cache[inp])
