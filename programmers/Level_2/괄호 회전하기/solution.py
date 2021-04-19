def check(s):
    answer = True
    q = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            q.append(c)
        else:
            try:
                if c == ')' and q[-1] == '(':
                    q.pop()
                elif c =='}' and q[-1] == '{':
                    q.pop()
                elif c == ']' and q[-1] == '[':
                    q.pop()
                else:
                    return False
            except:
                return False
    if len(q) == 0:
        return True
    return False
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        if check(s[i:] + s[:i]):
            answer += 1
    return answer