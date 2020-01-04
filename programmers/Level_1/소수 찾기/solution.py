import math

def solution(n):
    temp = [False] * (n + 1)
    r = math.sqrt(n)
    for i in range(2, len(temp)):
        if temp[i]:
            continue
        else:
            for j in range(2*i, n + 1, i):
                temp[j] = True
    
    count = 0
    for i in range(2, n + 1):
        if not temp[i]:
            count += 1
    return count