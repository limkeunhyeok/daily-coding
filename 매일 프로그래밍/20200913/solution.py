# 1~N 까지 있는 정수 배열에 원소 하나가 없어졌습니다. 없어진 원소의 값을 구하시오.

def solution(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) / 2   
    return total - sum(arr)