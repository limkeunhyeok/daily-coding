def d(n):
    selfNumber = n
    for i in str(n):
        selfNumber += int(i) 
    return selfNumber

arr = []

for i in range(1, 10000):
    k = d(i)
    arr.append(k)

for i in range(1, 1000):
    if i in arr:
        continue
    else:
        print(i)