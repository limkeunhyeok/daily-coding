def solution(n):
    d = 2
    while n != 1:
        if n % d == 0:
            n /= d
            print(d)
        else:
            d += 1

n = int(input())
solution(n)