def solution(n):
    dp = [0, 1, 2]
    for i in range(2, n):
        dp.append((dp[-1] + dp[-2]) % 10007)
    return dp[n]

n = int(input())
print(solution(n))