def solution(s):
    answer = ''
    count = 1
    for i in range(len(s)):
        if s[i] != ' ' and count % 2 == 1:
            answer += s[i].upper()
            count += 1
        else:
            answer += s[i].lower()
            count = 1
    return answer