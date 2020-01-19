def solution(n):
    answer = 0
    while True:
        if n == 0:
            break
        else:
            answer += n % 2
            n = n // 2
    return answer

def solution2(n):
    return bin(n).count('1')