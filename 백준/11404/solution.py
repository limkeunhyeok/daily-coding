import sys

input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())

matrix = [[INF for i in range(n)] for j in range(n)]

for _ in range(m):
    i, j, cost = map(int, input().split())
    if matrix[i - 1][j - 1] > cost:
        matrix[i - 1][j - 1] = cost

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == INF:
            print(0, end = ' ')
        else:
            print(matrix[i][j], end = ' ')
    print()