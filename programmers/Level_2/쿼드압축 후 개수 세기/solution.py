def quad(y, x, n, arr):
    if n == 1:
        return [0, 1] if arr[y][x] == 1 else [1,0]

    left_up = quad(y, x, (n // 2), arr)
    right_up = quad(y, (x + n // 2), (n // 2), arr)
    left_down = quad((y + n // 2), x, (n // 2), arr)
    right_down = quad((y + n // 2), (x + n // 2), (n // 2), arr)

    if (left_up == right_up == left_down == right_down == [0,1] or
        left_up == right_up == left_down == right_down == [1,0]):
        return left_up
    else:
        return list(map(sum, zip(left_up, right_up, right_down, left_down)))
    
def solution(arr):
    answer = quad(0, 0, len(arr), arr)
    return answer