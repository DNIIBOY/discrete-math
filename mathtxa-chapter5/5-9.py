def x1(n):
    if n == 0:
        return 1
    return x1(n-1) + n

def x2(n):
    if n == 0:
        return 2
    return x2(n-1) + n


if __name__ == "__main__":
    print([x1(i) for i in range(10)])
    print([x2(i) for i in range(10)])
