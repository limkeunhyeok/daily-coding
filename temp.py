import string

def solution(s, n):
    answer = ''
    s = list(s)
    alpha_low = list(string.ascii_lowercase)
    alpha_up = list(string.ascii_uppercase)

    for i in range(len(s)):
        if s[i].islower():
            answer += alpha_low[(alpha_low.index(s[i]) + n) % 26]
        if s[i].isupper():
            answer += alpha_up[(alpha_up.index(s[i]) + n) % 26]
        if s[i] == ' ':
            answer += ' '
    return answer

s = 'AB'
print(solution(s,1))