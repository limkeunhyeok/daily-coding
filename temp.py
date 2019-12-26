# 정규식 사용하지 않았을 때 풀이
def solution1(dartResult):
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

# 정규식 사용했을 때 풀이, 다른 사람의 풀이
import re

def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    
    answer = sum(dart)
    return answer