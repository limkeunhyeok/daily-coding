def solution(n):
    dp = [3, 11]
    
    for i in range(2, (n // 2)):
        temp = (dp[i - 1] + dp[i - 2]) % 1000000007
        dp.append(temp)
        
    return dp[-1]