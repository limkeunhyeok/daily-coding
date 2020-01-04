def solution(n):
    result = listConversion(n)
    result= descendingOrder(result)
    result = integerConversion(result)
    return result

def listConversion(n):
    result = list(map(int, str(n)))
    return result

def integerConversion(arr):
    arr = list(map(str, arr))
    arr = int("".join(arr))
    return int(arr)

def descendingOrder(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] <= arr[j]:
                valueA = arr[i]
                valueB = arr[j]
                arr[i] = valueB
                arr[j] = valueA
    return arr