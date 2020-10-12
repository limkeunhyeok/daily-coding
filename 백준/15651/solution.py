def backtracking(cnt, n, m):
    if cnt == m:
        print(*answer)
        return
    for i in range(1, n + 1):
        answer[cnt] = i
        backtracking(cnt + 1, n, m)

n, m = map(int, input().split(' '))
answer = [0] * m
backtracking(0, n, m)