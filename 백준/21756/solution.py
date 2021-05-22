import sys
input = sys.stdin.readline

def soluntion(n):
    arr = [i + 1 for i in range(n)]
    while True:
        if len(arr) == 1:
            return arr[0]
        temp = []
        for i in range(1, len(arr), 2):
            temp.append(arr[i])
        arr = temp

n = int(input())
print(soluntion(n))
