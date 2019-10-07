import math

def solution(brown, red):
    answer = []
    carpetArea = brown + red
    maximum = int(math.sqrt(carpetArea))

    # 빨간색 격자의 수는 (row - 2) * (col - 2)    
    for col in range(3, maximum + 1):
        if carpetArea % col == 0:
            row = int(carpetArea / col)
            if (row - 2) * (col - 2) == red:
                answer.append(row)
                answer.append(col)
                break
    return answer