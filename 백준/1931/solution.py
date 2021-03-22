N = int(input())
conference = []

for i in range(N):
    start, end = map(int, input().split(' '))
    conference.append([start, end])

conference.sort(key = lambda x: x[0])
conference.sort(key = lambda x: x[1])

last = 0
answer = 0

for i, j in conference:
    if i >= last:
        answer += 1
        last = j

print(answer)
