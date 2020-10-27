def solution(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp

dp = solution(40)
for T in range(int(input())):
    n = int(input())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:
        print(dp[n - 1], dp[n])

"""
전역 변수 사용, 시간초과
def solution(n):
    if n == 0:
        global cnt_zero
        cnt_zero += 1
        return 0
    elif n == 1:
        global cnt_one
        cnt_one += 1
        return 1
    else:
        return solution(n - 1) + solution(n - 2)

for T in range(int(input())):
    n = int(input())
    cnt_zero = 0
    cnt_one = 0
    solution(n)
    print(cnt_zero, cnt_one)
"""