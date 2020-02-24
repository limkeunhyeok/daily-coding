# 정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.

def solution(intArray):
    temp = sorted(intArray)
    if temp[-1] != temp[-2]:
        return temp[-2]
    else:
        return 'Does not exist.'