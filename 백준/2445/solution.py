if __name__ == "__main__":
    N = int(input())
    space = 0
    star = 0
    for i in range(1, N * 2):
        if i <= N:
            star = i
        else:
            star = N - (i % N)
        space = (N - star) * 2
        print("*" * star + " " * space + "*" * star)
        