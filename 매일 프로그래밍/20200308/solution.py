# 길이가 같은 두 문자열(string) A 와 B가 주어지면, A 가 B 로 1:1 암호화 가능한지 찾으시오.
def solution(firstString, secondString):
    encrypted = {}
    for i, c in enumerate(firstString):
        if c in list(encrypted.keys()):
            if encrypted[c] == secondString[i]:
                continue
            else:
                return False
        else:
            encrypted[c] = secondString[i]
            encrypted[secondString[i]] = c
    return True