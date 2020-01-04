def solution(n):
    value = n ** 0.5
    if int(value) == value:
        return (value + 1) ** 2
    else:
        return -1