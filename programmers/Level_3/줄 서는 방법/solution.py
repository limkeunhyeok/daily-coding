'''
내부 함수 permutations를 이용한 풀이
당연히 시간초과로 안된다
import itertools

def solution(n, k):
    answer = []
    for num in range(n):
        answer.append(str(num + 1))
    temp = list(map(''.join, itertools.permutations(answer)))
    return list(map(int, temp[k - 1]))
'''
import math

def solution(n, k):
    answer = []
    temp = [i + 1 for i in range(n)]
    for num in range(n - 1, 0, -1):
        answer.append(temp[k % math.factorial(num) + 1])
        temp.pop(k % math.factorial(num) + 1)
    answer.append(temp.pop(0))
    return answer
