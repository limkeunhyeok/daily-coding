import sys
input = sys.stdin.readline

def solution(x, y):
    dayOfWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    monthOfDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    
    total += sum(monthOfDay[:x - 1])
    total += y - 1
    q = total % 7
    print(dayOfWeek[q])
    
x, y = map(int, input().split())
solution(x, y)
