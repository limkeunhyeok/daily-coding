def solution(intervals):
    answer = []
    points = []
    for arr in intervals:
        points += list(range(arr[0], arr[1] + 1))
    points = list(set(points))
    
    temp = []
    for index in range(len(points) - 1):
        if not temp:
            temp.append(points[index])
        if points[index] - points[index + 1] != -1:
            temp.append(points[index])
            answer.append(temp)
            temp = []
        else:
            continue
    
    temp.append(points[-1])
    answer.append(temp)
    return answer