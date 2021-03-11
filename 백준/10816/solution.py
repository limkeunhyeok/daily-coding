def upperBound(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end
    
def lowerBound(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end

n = int(input())
cards = list(map(int, input().split(' ')))
m = int(input())
arr = list(map(int, input().split(' ')))
cards.sort()
answer = []

for i in range(m):
    answer.append(upperBound(cards, arr[i]) - lowerBound(cards, arr[i]))

print(*answer)