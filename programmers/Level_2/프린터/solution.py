def solution(priorities, location):
    answer = 0
    maxValue = max(priorities)
    while True:
        p = priorities.pop(0)
        if maxValue == p:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            maxValue = max(priorities)
        else:
            priorities.append(p)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return answer