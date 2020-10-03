def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left = list(divmod(n - 1, 3))
        
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right = list(divmod(n - 1, 3))
            
        else:
            if n == 0:
                if calcDist(left, [3, 1]) > calcDist(right,[3, 1]):
                    answer += 'R'
                    right = [3, 1]
                elif calcDist(left, [3, 1]) < calcDist(right, [3, 1]):
                    answer += 'L'
                    left = [3, 1]
                else:
                    if hand == 'left':
                        answer += 'L'
                        left = [3, 1]
                    else:
                        answer += 'R'
                        right = [3, 1]
            else:
                point = list(divmod(n - 1, 3))
                if calcDist(left, point) > calcDist(right, point):
                    answer += 'R'
                    right = point
                elif calcDist(left, point) < calcDist(right, point):
                    answer += 'L'
                    left = point
                else:
                    if hand == 'left':
                        answer += 'L'
                        left = point
                    else:
                        answer += 'R'
                        right = point
    return answer

def calcDist(curr, point):
    return abs(curr[0] - point[0]) + abs(curr[1] - point[1])