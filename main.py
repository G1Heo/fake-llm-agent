
def fibonacci(n):
    n = 10


    a, b = 1, 1

    for _ in range(n-2):
        a, b = b, a+b

    print(b)


if __name__ == '__main__':
    fibonacci(100)
