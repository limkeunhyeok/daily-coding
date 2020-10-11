n, m = map(int, input().split())
chess = []
answer = []

for _ in range(n):
    chess.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):
                if (j + b) % 2 == 0:
                    if chess[b][j] != 'W': idx1 += 1  
                    if chess[b][j] != 'B': idx2 += 1
                else :
                    if chess[b][j] != 'B': idx1 += 1
                    if chess[b][j] != 'W': idx2 += 1
        answer.append(idx1)
        answer.append(idx2)

print(min(answer))