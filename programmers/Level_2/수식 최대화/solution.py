import re
import itertools

def solution(expression):
    answer = 0
    numbers = re.findall('\d+', expression)
    operator = re.findall('\D', expression)
    priority = list(itertools.permutations(set(operator)))
        
    for testCase in priority:
        tempNum = list(map(int, numbers))
        tempOp = operator.copy()
        value = 0
        for op in testCase:
            for c in range(operator.count(op)):
                index = tempOp.index(op)
                value = eval('{}{}{}'.format(tempNum[index], op, tempNum[index + 1]))
                tempNum = tempNum[:index] + [value] + tempNum[index + 2:]
                tempOp.remove(op)
        if abs(tempNum[0]) > answer:
           answer = abs(tempNum[0])
    return answer

    