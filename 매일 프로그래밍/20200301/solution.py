# String이 주어지면, 중복된 char가 없는 가장 긴 서브스트링 (substring)의 길이를 찾으시오.

def solution(string):
    substring = []
    temp = ''
    for i in range(len(string)):
        if string[i] in temp:
            substring.append(temp)
            temp = string[i]
        else:
            temp += string[i]
    return longestLength(substring)

def longestLength(array):
    array.sort(key=len)
    return len(array[-1])