def solution(intArray):
    temp = sorted(intArray)
    if temp[-1] != temp[-2]:
        return temp[-2]
    else:
        return 'Does not exist.'