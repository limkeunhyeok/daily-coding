def solution(n):
    answer = []
    if n == 1:
        return 1
    for num in range(1, (n // 2) + 1):
        if n % num == 0:
            answer.append(num)
            answer.append(n / num)
    return sum(set(answer))