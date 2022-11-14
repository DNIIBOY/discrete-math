def a(n):
    if n == 1:
        return 1
    return a(n-1) + 2

def b(n):
    if n == 0:
        return 0
    return b(n-1) + 2

if __name__ == "__main__":
    print(a(5))
    print(b(4))
