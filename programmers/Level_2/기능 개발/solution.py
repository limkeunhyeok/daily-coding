import math

def solution(progresses, speeds):
    temp = []
    for i in range(len(progresses)):
        work = math.ceil((100 - progresses[i]) / speeds[i])
        temp.append(work)

    answer = []
    value = temp[0]
    count = 0
    for i in range(len(temp)):
        if temp[i] <= value:
            count += 1
        else:
            answer.append(count)
            count = 1
            value = temp[i]
    answer.append(count)
    return answer