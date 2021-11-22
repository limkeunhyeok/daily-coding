import itertools

def getAllWord():
    allWord = ['A','E','I','O','U']
    allWord.extend(list(map("".join, itertools.product('AEIOU',repeat=2))))
    allWord.extend(list(map("".join, itertools.product('AEIOU',repeat=3))))
    allWord.extend(list(map("".join, itertools.product('AEIOU',repeat=4))))
    allWord.extend(list(map("".join, itertools.product('AEIOU',repeat=5))))
    allWord.sort()
    return allWord

def solution(word):
    allWord = getAllWord()
    answer = allWord.index(word) + 1
    return answer