import sys
input = sys.stdin.readline

def solution(n):
    for i in range(n):
        temp = ' ' * i + '*' * (n - i)
        print(temp)

n = int(input())
solution(n)
