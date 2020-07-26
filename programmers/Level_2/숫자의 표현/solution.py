def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        value = 0
        for j in range(i, n + 1): 
            value += j 
            if value == n:
                answer += 1
                break
            elif value > n:
                break 
    return answer