import numpy as np

'''
// 다른 사람 풀이
def solution(arr1, arr2):
    answer = [[0] * len(arr2) for i in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
    
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
'''

def solution(arr1, arr2):
    arr = np.matmul(arr1, arr2)
    answer = []
    for i in arr:
        answer.append(list(i))
    return answer