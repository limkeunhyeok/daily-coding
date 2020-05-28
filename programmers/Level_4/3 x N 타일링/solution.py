def solution(n):
    dp = [1, 3]
    if (n // 2) <= 1:
        return dp[n // 2]
    
    for i in range(2, (n // 2) + 1):
        temp = (3 * dp[i - 1] + 2 * sum(dp[:i - 1])) % 1000000007
        dp.append(temp)
    return dp[-1]