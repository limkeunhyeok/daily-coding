def solution(x):
    arr = list(map(int, str(x)))
    if x % sum(arr) == 0:
        return True
    else:
        return False