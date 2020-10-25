# 카탈란 수
def solution(n):
    answer = 0
    a, b = 1, 1
    for i in range(2 * n, n, -1):
        a *= i
    for i in range(1, n + 1):
        b *= i    
    answer = (a / b) * (1 / (n + 1))
    return answer