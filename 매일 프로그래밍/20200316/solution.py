# 정수로된 배열이 주어지면, 각 원소가 자신을 뺀 나머지 원소들의 곱셈이 되게하라.
# 단, 나누기 사용 금지, O(n) 시간복잡도

def solution(intArray):
    initial = 1
    one = [0] * len(intArray)
    two = [0] * len(intArray)
    
    for i in range(len(intArray)):
        one[i] = initial
        initial *= intArray[i]
    
    initial = 1
    for i in range(len(intArray) - 1, -1, -1):
        two[i] = initial
        initial *= intArray[i]

    answer = []
    for i in range(len(intArray)):
        answer.append(one[i] * two[i])
    return answer