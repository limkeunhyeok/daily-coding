import math

def solution(n,a,b):
    answer = 0
    while True:
        if math.ceil(a / 2) == math.ceil(b / 2):
            return answer + 1
        else:
            a = math.ceil(a / 2)
            b = math.ceil(b / 2)
            answer += 1