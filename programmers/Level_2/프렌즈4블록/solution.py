def delete(m, n, board):
    temp = ['' for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                temp[j] = board[i][j] + temp[j]
            else:
                temp[j] += board[i][j]
    for i in range(n):
        for j in range(m):
            board[j][i] = temp[i][j]
    return board

def solution(m, n, board):
    answer = 0
    board = [list(s) for s in board]
    while True:
        check = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == 'X':
                    continue
                elif board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    if [i, j] not in check:
                        check.append([i, j])
                    if [i, j + 1] not in check:
                        check.append([i, j + 1])
                    if [i + 1, j] not in check:
                        check.append([i + 1, j])
                    if [i + 1, j + 1] not in check:
                        check.append([i + 1, j + 1])
        if not check:
            break
        else:
            answer += len(check)
            for c in check:
                board[c[0]][c[1]] = 'X'
            board = delete(m, n, board)
    return answer