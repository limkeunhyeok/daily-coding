def solution(n, r, c):
    answer = 0
    while n > 0:
        temp = (2 ** n) // 2
        if n > 1:
            if temp > r and temp <= c:
                answer += temp ** 2
                c -= temp
            elif temp <= r and temp > c:
                answer += (temp ** 2) * 2
                r -= temp
            elif temp <= r and temp <= c:
                answer += (temp ** 2) * 3
                r -= temp
                c -= temp
        elif n == 1:
            if r == 0 and c == 1:
                answer += 1
            elif r == 1 and c == 0:
                answer += 2
            elif r == 1 and c == 1:
                answer += 3
        n -= 1
    return answer

n, r, c = map(int, input().split())
print(solution(n, r, c))