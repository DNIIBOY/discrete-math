def x(n):
    if n == 0:
        return 1500
    return 1.0115 * x(n-1)


if __name__ == "__main__":
    print([round(x(i), 2) for i in range(10)])
