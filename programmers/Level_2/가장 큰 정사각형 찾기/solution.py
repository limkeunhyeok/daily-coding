def solution(board):
    check = 0
    for i in range(len(board)):
        check += sum(board[i])
    if check == 0:
        return 0
    elif check == 1:
        return 1
    else:
        temp = board
        max_length = 0
        for i in range(1, len(board)):
            for j in range(1, len(board[i])):
                if temp[i][j]:
                    temp[i][j] += min(temp[i - 1][j], temp[i][j - 1], temp[i - 1][j - 1])
                    max_length = max(max_length, temp[i][j])
        return max_length ** 2