import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
num = [0]

for i in range(N):
    num.append(num[-1] + arr[i])

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(num[j])
    else:
        print(num[j] - num[i - 1])