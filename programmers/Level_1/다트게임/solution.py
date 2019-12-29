def solution(dartResult):
    number = ''
    temp = []
    for c in dartResult:
        if c.isdigit():
            number += c
        elif c == 'S':
            temp.append(int(number))
            number = ''
        elif c == 'D':
            temp.append(int(number) ** 2)
            number = ''
        elif c == 'T':
            temp.append(int(number) ** 3)
            number = ''
        elif c == '#':
            temp[-1] = temp[-1] * (-1)
            number = ''
        elif c == '*':
            if len(temp) == 1:
                temp[0] = temp[0] * 2
            else:
                temp[-1] = temp[-1] * 2
                temp[-2] = temp[-2] * 2
    return sum(temp)