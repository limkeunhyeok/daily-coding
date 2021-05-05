import sys

def push(q, x):
    q.append(x)
    return q

def pop(q):
    if q:
        print(q.pop(0))
    else:
        print(-1)

def size(q):
    print(len(q))

def empty(q):
    if q:
        print(0)
    else:
        print(1)

def front(q):
    if q:
        print(q[0])
    else:
        print(-1)

def back(q):
    if q:
        print(q[-1])
    else:
        print(-1)

d = {
     'push': push,
     'pop': pop,
     'size': size,
     'empty': empty,
     'front': front,
     'back': back
}

q = []

n = int(sys.stdin.readline())
for _ in range(n):
    commands = sys.stdin.readline().split()
    if len(commands) == 1:
        command = commands[0]
        d[command](q)
    else:
        command, x = commands
        q = d[command](q, x)