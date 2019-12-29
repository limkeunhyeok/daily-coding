def solution(n):
    answer = ''
    arr = ['4','1','2']
    while n > 0:
        x = n % 3
        n = n // 3
        if x == 0:
            n -= 1
        answer += arr[x]
    return answer[::-1]