def solution(n):
    arr = [0, 1]
    for i in range(n - 2):
        arr.append(sum(arr) % 1234567)
        arr.remove(arr[0])
    return sum(arr)