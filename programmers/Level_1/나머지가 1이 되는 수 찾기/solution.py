def getMinNumber(number):
    for num in range(2, number):
        if number % num == 1:
            return num

def solution(n):
    answer = getMinNumber(n)
    return answer