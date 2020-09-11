# 반복된 알파벳으로 이루어진 문자배열이 주어지면 연속으로 중복된 알파벳이 없도록 문자배열을 재배열하여 리턴하시오.
# 불가능 하다면 empty string을 리턴하시오.

def solution(s):
    answer = ''
    q = []
    s = list(s)
    answer += s.pop(0)
    while s:
        if not q:
            if answer[-1] != s[0]:
                answer += s.pop(0)
            else:
                q.append(s.pop(0))
        else:
            if answer[-1] != q[0]:
                answer += q.pop(0)
            elif answer[-1] != s[0]:
                answer += s.pop(0)
            else:
                q.append(s.pop(0))
    
    if q and answer[-1] != q[0]:
        answer += q.pop(0)
        
    if not q:
        return answer
    return ""