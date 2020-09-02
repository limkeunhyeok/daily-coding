# 정수 배열과 정수 k가 주어지면 모든 원소를 k칸씩 앞으로 옮기시오.
def solution1(arr, k):
    return arr[k:] + arr[:k]

def solution2(arr, k):
    temp = []
    for _ in range(k):
        temp.append(arr.pop(0))
    return arr + temp