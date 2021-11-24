if __name__ == "__main__":
    N = int(input())
    space = 0
    star = 0
    for i in range(1, N * 2):
        if i < N:
            space = N - i
        else:
            space = i - N
        star = 2 * (N -space) - 1
        print(" " * space + "*" * star)
        