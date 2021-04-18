def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    answer = []
    temp = 0
    while arr:
        temp = (temp + k - 1) % len(arr)
        answer.append(arr.pop(temp))
    return answer

def show(arr):
    answer = '<'
    for n in arr:
        answer += str(n) + ', '
    answer = answer[:-2] + '>'
    print(answer)

n, k = map(int, input().split(' '))
show(solution(n, k))
