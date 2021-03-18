num = int(input())
n = int(input())

while n:
    if n % num == 0:
        print("%s is a multiple of %s." % (n, num))
    else:
        print("%s is NOT a multiple of %s." % (n, num))
    n = int(input())