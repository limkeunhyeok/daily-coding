def Floyd_Warshall(matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] or (matrix[i][k] and matrix[k][j]):
                    matrix[i][j] = 1
    return matrix

def show(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                print(1, end = ' ')
            else:
                print(0, end = ' ')
        print()

def solution(matrix, n):
    matrix = Floyd_Warshall(matrix, n)
    show(matrix, n)

n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

solution(matrix, n)