def solution(n):
    answer = [0]
    if n == 1:
        return answer
    else:
        for i in range(n - 1):
            temp = answer
            temp = converter(temp)
            answer.append(0)
            answer += temp
    return answer

def converter(arr):
    res = []
    for num in arr:
        if num == 0:
            res.append(1)
        else:
            res.append(0)
    res.reverse()
    return res