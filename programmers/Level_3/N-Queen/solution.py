def promising(i, col):
    k = 0
    correct = True
    while (k < i and correct):
        if (col[i] == col[k] or abs(col[i] - col[k]) == i - k):
            correct = False
            break
        k += 1
    return correct

def nqueen(n, i, col, count):
    if (promising(i, col)):
        if (i == n - 1):
            count.append(col)
        else:
            for j in range(n):
                col[i + 1] = j
                nqueen(n, i + 1, col, count)

def solution(n):
    col = n * [0]
    global count
    count = []
    nqueen(n, -1, col, count)
    return len(count)