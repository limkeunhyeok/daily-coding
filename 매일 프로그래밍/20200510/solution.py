# 정수 배열 arr이 있습니다. arr안의 각 원소의 값은 다음 원소의 인덱스입니다.
# 이렇게 서로 이어지는 원소들의 배열이 있을때, arr[0]부터 시작하여 모든 원소를 들린 다음 다시 arr[0]로 도착할 수 있는지 찾으시오.
# 단, 시간복잡도는 O(n), 공간복잡도는 O(1).

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