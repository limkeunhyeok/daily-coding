def makeBoard(rows, columns):
    answer = []
    num = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(num)
            num += 1
        answer.append(temp)
    return answer

def rotate(query, board):
    x1, y1, x2, y2 = query
    temp = board[x1 - 1][y2 - 1]
    minValue = temp
    minValue = min(min(board[x1 - 1][y1 - 1:y2 - 1]), minValue)
    board[x1 - 1][y1:y2] = board[x1 - 1][y1 - 1:y2 - 1]
    
    for i in range(x1, x2):
        minValue = min(board[i][y1 - 1], minValue)
        board[i - 1][y1 - 1] = board[i][y1 - 1]
        
    minValue = min(min(board[x2 - 1][y1:y2]), minValue)
    board[x2 - 1][y1 - 1:y2 - 1] = board[x2 - 1][y1:y2]
    
    for i in range(x2 - 2, x1 - 2, -1):
        minValue = min(board[i][y2 - 1], minValue)
        board[i + 1][y2 - 1] = board[i][y2 - 1]
        
    board[x1][y2 - 1] = temp
    return board, minValue

def solution(rows, columns, queries):
    answer = []
    board = makeBoard(rows, columns)

    for query in queries:
        board, minValue = rotate(query, board)
        answer.append(minValue)
    return answer