from collections import deque

n, m = map(int, input().split(' '))
q = deque(range(1, n + 1))

numbers = list(map(int, input().split(' ')))
answer = 0

for num in numbers:
    index = q.index(num)
    if len(q) - index < index:
        index = len(q) - index
    else:
        index *= -1
    q.rotate(index)
    answer += abs(index)
    q.popleft()
    
print(answer)