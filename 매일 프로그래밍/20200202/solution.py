# 간격(interval)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오.
# 간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.

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