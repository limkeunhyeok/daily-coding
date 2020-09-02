def solution(arr):
    index = 0
    total = 0
    arrSum = sum([_ for _ in range(len(arr))])
    
    for _ in range(len(arr)):
        if index == arr[index]:
            print()
            return False
        index = arr[index]
        total += index
        print(index, end=' ')

    print()
    if total != arrSum:
        return False
    return True