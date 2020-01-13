# 정수 n이 주어질 때 괄호로 만들 수 있는 모든 조합을 구하여라
def solution(n):
    dp = ["()"]
    for i in range(n - 1):
        temp = []
        for j in range(len(dp)):
            temp.append("(" + dp[j] + ")")
            temp.append("()" + dp[j])
            temp.append(dp[j] + "()")
        dp = list(set(temp))
    return dp

# dp를 이용한 풀이
# 예제 답안의 경우의 수 순서는 고려하지 않음