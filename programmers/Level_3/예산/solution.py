import math

def solution(budgets, M):
    answer = 0
    temp = []
    budgets = sorted(budgets)
    for index, value in enumerate(budgets):
        if value * (len(budgets) - index) < M:
            M -= value
        elif value * (len(budgets) - index) == M:
            return value
        else:
            temp = [budgets[index - 1]] * (len(budgets) - index)
            break
    
    if len(temp) == 0:
        return budgets[-1]
    answer = math.floor((M - sum(temp)) / len(temp)) + temp[0]
    return answer