import sys
input = sys.stdin.readline

def solution(numbers):
    numbers.sort();
    print(numbers[1])

numbers = list(map(int, input().split()))
solution(numbers)
