def solution(a,b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = b - 1
    for i in range(a - 1):
        sum += months[i]
    answer = days[sum%7]
    return answer