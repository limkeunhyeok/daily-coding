def solution(n, money):
    table = [[0 for _ in range(n + 1)] for _ in range(len(money))]
    table[0][0] = 1
    
    for i in range(money[0], n + 1, money[0]):
        table[0][i] = 1
    
    for i in range(1, len(money)):
        for j in range(n + 1):
            if j >= money[i]:
                table[i][j] = (table[i - 1][j] + table[i][j - money[i]]) %  1000000007
            else:
                table[i][j] = table[i - 1][j]
    return table[-1][-1]