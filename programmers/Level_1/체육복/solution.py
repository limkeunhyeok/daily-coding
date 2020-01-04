def solution(n, lost, reserve):
    clothes = [1] * n
    for index in lost:
        clothes[index - 1] -= 1
    for index in reserve:
        clothes[index - 1] += 1
        
    for index in range(n - 1):
        if abs(clothes[index] - clothes[index + 1]) == 2:
            clothes[index] = 1
            clothes[index + 1] = 1
    for index in range(n):
        if clothes[index] == 0:
            n -= 1
    return n