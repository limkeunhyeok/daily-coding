def solution(s):
    answer = ''
    text = sorted(s)
    for i in text[::-1]:
        answer += i
    return answer