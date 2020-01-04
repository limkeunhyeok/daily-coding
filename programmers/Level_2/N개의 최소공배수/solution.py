def solution(arr):
    answer = arr[0]
    for i in range(len(arr) - 1):
        answer = lcm(answer, arr[i + 1])
    return answer
    
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def lcm(a, b):
    return a * b / gcd(a, b)