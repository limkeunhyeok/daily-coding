def solution(n):
    dp = [1, 1]
    for i in range(1, n):
        dp.append(dp[-1] + dp[-2])
    return dp[-1] % 1234567