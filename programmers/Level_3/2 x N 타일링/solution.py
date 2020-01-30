def solution(n):
    dp = [1, 2]
    for count in range(n - 2):
        dp.append(dp[0] + dp[1])
        dp.pop(0)
    return dp[-1] % 1000000007

'''
다른 사람 풀이
효율성 테스트에서 실행 시간이 더 빠름
def solution(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a % 1000000007
'''