def x(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return 4*x(n-1) - 3*x(n-2) + 5*n + 2

if __name__ == "__main__":
    print([x(n) for n in range()])

