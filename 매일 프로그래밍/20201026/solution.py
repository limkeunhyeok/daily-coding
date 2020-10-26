# 정수 배열과 정수 K가 주어지면 원소 3개의 합으로 K가 만들어지는지 체크하시오.

def solution(arr, k):
    answer = []
    arr.sort()
    
    for i in range(len(arr) - 2):
        start = i + 1
        end = len(arr) - 1
        while start < end:
            if arr[i] + arr[start] + arr[end] == k:
                answer.append([arr[i], arr[start], arr[end]])
                start += 1
            elif arr[i] + arr[start] + arr[end] < k:
                start += 1
            else:
                end -= 1
    return answer