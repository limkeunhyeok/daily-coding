if __name__ == "__main__":
    N = int(input())
    space = 0
    star = 0
    for i in range(N, 0, -1):
        space = N - i
        star = i * 2 - 1
        print(" " * space + "*" * star)
        