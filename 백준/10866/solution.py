import sys

def push_front(deq, x):
    temp = [x]
    temp.extend(deq)
    deq = temp
    return deq

def push_back(deq, x):
    deq.append(x)
    return deq

def pop_front(deq):
    if deq:
        print(deq.pop(0))
    else:
        print(-1)

def pop_back(deq):
    if deq:
        print(deq.pop())
    else:
        print(-1)
    
def size(deq):
    print(len(deq))
    
def empty(deq):
    if deq:
        print(0)
    else:
        print(1)

def front(deq):
    if deq:
        print(deq[0])
    else:
        print(-1)

def back(deq):
    if deq:
        print(deq[-1])
    else:
        print(-1)

d = {
     'push_front': push_front,
     'push_back': push_back,
     'pop_front': pop_front,
     'pop_back': pop_back,
     'size': size,
     'empty': empty,
     'front': front,
     'back': back
}

deq = []
n = int(sys.stdin.readline())
for _ in range(n):
    commands = sys.stdin.readline().split()
    if len(commands) == 1:
        command = commands[0]
        d[command](deq)
    else:
        command, x = commands
        deq = d[command](deq, x)
