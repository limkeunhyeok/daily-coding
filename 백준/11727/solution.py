def solution(n):
    dp = [0, 1, 3]
    for i in range(3, n + 1):
        temp = dp[i - 1] + (dp[i - 2] * 2)
        dp.append(temp % 10007)
    print(dp[n])

n = int(input())
solution(n)
