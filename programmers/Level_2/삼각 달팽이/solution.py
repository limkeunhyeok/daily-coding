def solution(n):
    answer = []
    temp = [[0] * i for i in range(1, n + 1)]
    
    rowIndex, colIndex = 0, 0
    num = 1
    
    while n != 0:
        for i in range(n):
            temp[rowIndex][colIndex] = num
            num += 1
            rowIndex += 1
        n -= 1
        if n == 0:
            break
        colIndex += 1
        rowIndex -= 1
        
        for i in range(n):
            temp[rowIndex][colIndex] = num
            num += 1
            colIndex += 1
        n -= 1
        if n == 0:
            break
        rowIndex -= 1
        colIndex -= 2
        
        for i in range(n):
            temp[rowIndex][colIndex] = num
            num += 1
            rowIndex -= 1
            colIndex -= 1
        n -= 1
        if n == 0:
            break
        rowIndex += 2
        colIndex += 1
    
    for level in temp:
        answer += level
    return answer