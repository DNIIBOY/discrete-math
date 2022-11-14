def a(n):
    if n == 0:
        return 0
    return a(n-1) + n**2

def b(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return 2*b(n-1) + b(n-2)



def c(n):
    if n == 0:
        return 2
    if n == 1:
        return 4
    if n == 2:
        return 11
    return c(n-1) + 2 * c(n-2) + 5 * c(n-3)


if __name__ == "__main__":
    print([a(i) for i in range(1, 16)])
    print([b(i) for i in range(2, 17)])
    print([c(i) for i in range(3, 18)])
