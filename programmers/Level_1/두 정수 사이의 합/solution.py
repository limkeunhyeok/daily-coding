def solution(a, b):
    sum = 0
    if a > b:
        for i in range(b,a+1):
            sum += i
        return sum
    elif a < b:
        for i in range(a,b+1):
            sum += i
        return sum
    else:
        return a