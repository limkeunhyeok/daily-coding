def solution(s):
    temp = []
    index = 0
    while index != len(s):
        temp.append(s[index])
        index += 1
        if len(temp) > 1:
            if temp[-1] == temp[-2]:
                temp.pop()
                temp.pop()
    if len(temp) == 0:
        return 1
    else:
        return 0