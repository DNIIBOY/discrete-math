def x(n):
    if n == 0:
        return 1000
    return 1.2 * x(n-1)


if __name__ == "__main__":
    print([round(x(i), 1) for i in range(1, 11)])
    
