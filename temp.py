def solution(board, moves):
    temp = [0] * len(board[0])
    for i in range(len(board[0])):
        temp[i] = topDoll(i, board)
    
    backet = []
    answer = 0
    for i in moves:
        if temp[i - 1] != 0:
            if bool(backet) and backet[-1] == temp[i - 1]:
                answer += 2
                del backet[-1]
                board = move(i - 1, board)
                temp[i - 1] = topDoll(i - 1, board)
                continue
            else:
                backet.append(temp[i - 1])
                board = move(i - 1, board)
                temp[i - 1] = topDoll(i - 1, board)
                continue
        else:
            continue
    return answer

def topDoll(index, board):
    for i in range(len(board)):
        if board[i][index] != 0:
            return board[i][index]
    return 0

def move(index, board):
    for i in range(len(board)):
        if board[i][index] != 0:
            board[i][index] = 0
            return board
    return board


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
