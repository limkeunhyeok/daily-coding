def solution(arr, n):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return 1
        elif arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
arr = list(map(int, input().split(' ')))

m = int(input())
search = list(map(int, input().split(' ')))

arr.sort()
for i in range(m):
    print(solution(arr, search[i]))
    