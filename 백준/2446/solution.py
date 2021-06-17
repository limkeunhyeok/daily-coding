num = int(input())

space = -1
for i in range(num * 2 - 1):
    if (i < num):
        space += 1
    else:
        space -= 1
    star = (num - space) * 2 - 1
    string = ' ' * space + '*' * star
    print(string)
