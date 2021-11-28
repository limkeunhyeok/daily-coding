if __name__ == "__main__":
    A, B, C = map(int, input().split(" "))
    N = int(input())
    group = []

    for i in range(N):
        score = 0
        for j in range(3):
            a, b, c = map(int, input().split(" "))
            score += a * A + b * B + c * C
        group.append(score)
    print(max(group))