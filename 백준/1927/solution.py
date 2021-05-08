from queue import PriorityQueue
import sys
input = sys.stdin.readline

q = PriorityQueue()

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if q.empty():
            print(0)
        else:
            print(q.get())
    else:
        q.put(n)
