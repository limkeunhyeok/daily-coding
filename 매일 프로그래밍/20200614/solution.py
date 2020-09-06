# 정렬된 정수 배열이 있습니다. 이 배열의 모든 원소들을 오른쪽으로 랜덤하게 Z번 이동하였습니다.
# 예를 들면 [1, 2, 3, 4, 5] -> [3, 4, 5, 1, 2].
# 이런 배열과 정수 K 가 주어지면, 배열안에 K가 존재하는지 찾으시오.
# 존재한다면 배열의 인덱스, 존재하지 않다면 -1 을 리턴하시오.
# 시간복잡도 제한 O(log N).

def solution(arr, k):
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    
    while True:
        if arr[mid] == k:
            return 1
        
        if mid == start or mid == end:
            return -1
        
        if arr[mid] > k:
            end = mid
            mid = (start + end) // 2
        else:
            start = mid
            mid = (start + end) // 2