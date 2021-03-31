def solution(a, b):
    answer = 1
    while True:
        if b == a:
            break
        elif (b % 2 != 0 and b % 10 != 1) or b < a:
            answer = -1
            break
        else:
            if b % 10 == 1:
                b //= 10
                answer += 1
            else:
                b //= 2
                answer += 1
    return answer

a, b = map(int, input().split())
print(solution(a, b))