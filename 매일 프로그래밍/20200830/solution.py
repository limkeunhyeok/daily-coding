# 주어진 정수가 4의 거듭제곱인지 확인하시오.

def solution(n):
    while n != 1:
        if n % 4 == 0:
            n = n / 4
        else:
            return False
    return True