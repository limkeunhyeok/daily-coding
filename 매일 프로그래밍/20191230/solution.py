def solution(array):
    maxSum = -987654321
    for index in range(len(array)):
        if maxSum < sum(array[index:]):
            maxSum = sum(array[index:])
    return maxSum