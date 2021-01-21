# 0과 1로만 구성된 바이너리 배열이 주어졌을 때, 0과 1의 원소의 수가 같은 최대 길이의 부분 배열을 구하시오.
# 부분 배열은 배열 내의 연속된 원소들의 집합입니다.

def arrReplace(arr, old, new):
    answer = []
    for i in range(len(arr)):
        if arr[i] == old:
            answer.append(new)
        else:
            answer.append(arr[i])
    return answer

def solution(arr):
    answer = []
    newArr = arrReplace(arr, 0, -1)
    length = len(arr)
    flag = False
    
    for i in range(length):
        temp = length - i
        for j in range(i):
            if sum(newArr[j:temp + j]) == 0:
                answer.append(arr[j:temp + j])
                flag = True
        if flag:
            return answer
    return answer