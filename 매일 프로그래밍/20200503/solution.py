# 2차 정수 배열(2D int array)가 주어지면, 소용돌이 모양으로 원소들을 프린트하시오.

def solution(arr):
    answer = ''
    rowIndex, colIndex = 0, 0
    maxRow, maxCol = len(arr), len(arr[0])
    
    while (rowIndex < maxRow and colIndex < maxCol):
        for i in range(colIndex, maxCol):
            answer += str(arr[rowIndex][i]) + ', '
        rowIndex += 1

        for i in range(rowIndex, maxRow):
            answer += str(arr[i][maxCol - 1]) + ', '
        maxCol -= 1
  
        if (rowIndex < maxRow):
            for i in range(maxCol - 1, (colIndex - 1), -1) : 
                answer += str(arr[maxRow - 1][i]) + ', '
            maxRow -= 1

        if (colIndex < maxCol) : 
            for i in range(maxRow - 1, rowIndex - 1, -1) : 
                answer += str(arr[i][colIndex]) + ', '
            colIndex += 1
    return answer[:-2]