import itertools
import math

def isPrime(num):
    if num <= 1:
        return False
    r = int(math.sqrt(num))
    for i in range(2,r+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    r = len(numbers)
    for i in range(r):
        temp = list(map(''.join, itertools.permutations(numbers,r-i)))
        for j in temp:
            if isPrime(int(j)):
                answer.append(int(j))
    answer = list(set(answer))
    return len(answer)