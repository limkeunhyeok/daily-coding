import sys
input = sys.stdin.readline

def solution(n, k):
    answer = 1
    for i in range(n, n - k, -1):
        answer *= i
    for i in range(k, 0, -1):
        answer //= i
    print(answer)

n, k = map(int, input().split())
solution(n, k)
