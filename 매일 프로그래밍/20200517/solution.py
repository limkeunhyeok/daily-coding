# O(n log n)시간 복잡도를 가진 정수 배열 정렬 알고리즘을 구현하시오.

# 합병 정렬
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        leftArr = merge_sort(left)
        rightArr = merge_sort(right)
        return merge(leftArr, rightArr)
    else:
        return arr

def merge(left, right):
    i = 0
    j = 0
    arr = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    
    while i < len(left):
        arr.append(left[i])
        i += 1
    
    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr

# 퀵 정렬
def quick_sort(arr):
     if len(arr) < 2:
        return arr

     pivot = arr[0]
     left = [num for num in arr[1:] if num < pivot]
     right = [num for num in arr[1:] if num >= pivot]
     
     arr = quick_sort(left) + [pivot] + quick_sort(right)
     return arr