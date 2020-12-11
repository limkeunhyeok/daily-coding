def check(s):
    temp = []
    for c in s:
        if c == '(':
            temp.append(c)
        elif temp:
            temp.pop()
    return not temp

def divide(s):
    temp = 0
    for i in range(len(s)):
        if s[i] == '(':
            temp += 1
        else:
            temp -= 1
        if temp == 0:
            return s[:i + 1], s[i + 1:]

def solution(p):
    answer = ''
    if not p:
        return ''
    
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        
        for c in u[1:len(u) - 1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('
        return answer