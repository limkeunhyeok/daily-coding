# 중복된 원소가 없는 정렬된 배열이 있습니다. 이 배열에서 원소의 값이 원소의 인덱스 값과 같다면 프린트 하시오. 시간복잡도 O(log n).

def magicIndex(arr, start, end): 
    if (start > end): 
        return -1
  
    midIndex = (start + end) // 2  
    midValue = arr[midIndex]  
  
    if (midIndex == midValue): 
        return midIndex  
  
    left = magicIndex(arr, start, min(midValue, midIndex - 1))  
  
    if (left >= 0): 
        return left  
  
    return magicIndex(arr, max(midValue, midIndex + 1), end)


def solution(arr):
    start = 0
    end = len(arr) - 1     
    return magicIndex(arr, start, end)