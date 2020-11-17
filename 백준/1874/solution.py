number = int(input())
arr = list(range(1, number + 1))
stack = []
temp = []
answer = []

for _ in range(number):
    n = int(input())
    if stack and stack[-1] == n:
        answer.append('-')
        temp.append(stack.pop())
    elif n in arr:
        while True:
            answer.append('+')
            stack.append(arr.pop(0))
            if stack[-1] == n:
                answer.append('-')
                temp.append(stack.pop())
                break
    elif n in stack:
        if n == stack[-1]:
            answer.append('-')
            temp.append(stack.pop())
        else:
            answer.append('NO')
    else:
        answer.append('NO')

if 'NO' in answer:
    print('NO')
else:
    for i in answer:
        print(i)