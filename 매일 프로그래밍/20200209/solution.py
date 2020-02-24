# 주어진 string 에 모든 단어를 거꾸로 하시오.

def solution(s):
    answer = ''
    words = s.split(' ')
    
    for word in words:
        answer += reverseWord(word) + ' '
    return answer[:-1]

def reverseWord(w):
    return w[::-1]