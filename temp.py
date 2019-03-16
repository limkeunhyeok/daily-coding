def solution(s):
    answer = True
    countp = 0
    county = 0
    for i in s:
        if i == 'p' or i == 'P':
            countp += 1
        if i == 'y' or i == 'Y':
            county += 1
    if countp == county or (countp == county == 0):
        return True
    else:
        return False