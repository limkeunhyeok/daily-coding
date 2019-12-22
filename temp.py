def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = format((arr1[i] | arr2[i]), 'b')
        temp = temp.replace('1', '#').replace('0',' ')
        if len(temp) != n:
            space = (n - len(temp)) * ' '
            temp = space + temp
        answer.append(temp)
    return answer