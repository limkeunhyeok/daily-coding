def solution(n):
    if n == 1:
        return 1
    answer = 0
    num = ''
    while True:
        n, r = divmod(n, 3)
        if n <= 2:
            num += str(r)
            num += str(n)
            break
        else:
            num += str(r)
    l = len(num)
    for i in range(l):
        answer += int(num[l - i - 1]) * (3 ** i)
    return answer