num = int(input())

for i in range(-num + 1, num):
    print('*' * (num - abs(i)))
