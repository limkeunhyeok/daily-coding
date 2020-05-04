def solution(s):
    answer = 1
    
    for i in range(len(s)):
        for j in range(i + answer, len(s) + 1):
            temp = s[i:j]
            if temp == temp[::-1]:
                if answer < len(temp):
                    answer = len(temp)
    return answer