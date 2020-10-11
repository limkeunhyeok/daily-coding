from collections import Counter
import sys

def calc1(arr, n):
    return round(sum(arr) / n)

def calc2(arr, n):
    return arr[n // 2]

def calc3(arr, n):
    mode_dict = Counter(arr)
    modes = mode_dict.most_common()    
    if n > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]
    return mod

def calc4(arr):
    return arr[-1] - arr[0]

arr = []
n = int(input())

for T in range(n):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)
print(calc1(arr, n))
print(calc2(arr, n))
print(calc3(arr, n))
print(calc4(arr))