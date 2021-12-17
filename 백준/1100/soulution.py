if __name__ == "__main__":
    board = []
    for _ in range(8):
        row = input()
        board.append(row)
    
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "F" and (i + j) % 2 == 0:
                count += 1
    print(count)
