# 크기가 n인 배열에 1부터 n-1까지의 수가 들어 있고,
# 중복된 수가 한 개 더 들어 있다고 할 때,
# 중복된 수가 무엇인지 찾으시오.

def solution1(arr):
    n = len(arr)
    answer = sum(arr) - n * (n - 1) / 2
    return answer

def solution2(arr):
    n = len(arr)
    check = set(range(1, n))
    for v in arr:
        if v in check:
            check -= {v}
        else:
            return v