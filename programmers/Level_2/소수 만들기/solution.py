import itertools

def solution(nums):
    answer = 0
    comb = combList(nums)
    for i in range(len(comb)):
        if isPrime(intSum(comb[i])):
            answer += 1
    return answer
        

def isPrime(num):
    if num <= 1:
        return False
    else:
        d = int(num ** 0.5)
        for n in range(2, d + 1):
            if num % n == 0:
                return False
        return True

def intSum(partList):
    partList = list(map(int, partList))
    return sum(partList)

def combList(nums):
    nums = list(map(str, nums))
    result = list(map(list, itertools.combinations(nums, 3)))
    return result

'''
다른 사람 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
'''