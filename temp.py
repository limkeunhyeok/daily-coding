def solution(n, t, m, p):
    temp = ''
    answer = ''
    num = 0
    while True:
        if len(temp) >= t * m:
            break
        else:
            temp += convert(num, n)
            num += 1
    
    p -= 1
    while len(answer) != t:
        answer += temp[p]
        p += 2
    return answer

# 2~16진수 변환
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]