# 정렬(sort)된 정수 배열과 정수 n이 주어지면, 배열안에 n이 있는지 체크하시오. 시간복잡도를 최대한 최적화하시오.

def solution(arr, n):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    
    while True:
        if arr[start] > n or arr[end] < n:
            return False
        else:
            if arr[mid] is n:
                return True
            elif arr[mid] > n:
                end = mid
                mid = (start + end) // 2
            else:
                start = mid
                mid = (start + end) // 2