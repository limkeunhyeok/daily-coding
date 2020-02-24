def solution(s):
    answer = ''
    words = s.split(' ')
    
    for word in words:
        answer += reverseWord(word) + ' '
    return answer[:-1]

def reverseWord(w):
    return w[::-1]