# 정수 배열과 정수 S가 주어졌을 때, 원소의 합이 S와 같은 가장 긴 부분 배열을 구하시오.
# 부분 배열은 배열 내의 연속된 원소들의 집합입니다.

def solution(arr, s):
    subArray = []
    start, end = 0, 0
    n = len(arr)
    while start <= n and end <= n:
        if end >= n:
            if s == sum(arr[start:end]):
                subArray.append(arr[start:end])
            start += 1
        else:
            temp = sum(arr[start:end])
            if s == temp:
                subArray.append(arr[start:end])
                start += 1
            elif s > temp:
                end += 1
            else:
                start += 1
    subArray = sorted(subArray)
    return subArray[0]