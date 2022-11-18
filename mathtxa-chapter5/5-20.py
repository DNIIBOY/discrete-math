def x(n):
    if n == 0:
        return 3
    return x(n-1) + 4

if __name__ == "__main__":
    print([x(n) for n in range(11)])
