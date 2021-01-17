"""
# 메모리 초과
def solution(k):
    dp = ['4', '7']
    if k <= 2:
        return int(dp[k - 1])
    
    count = 0
    while len(dp) <= k:
        print(dp)
        temp = dp[count:].copy()
        print(temp)
        for num in temp:
            dp.append('4' + num)
        for num in temp:
            dp.append('7' + num)
        count += len(temp)
    print(dp)
    return int(dp[k - 1])
"""

def solution(k):
    answer = bin(k + 1)[3:]
    return answer.replace('0', '4').replace('1', '7')

k = int(input())
print(solution(k))