import sys
input = sys.stdin.readline
    
string = input()
length = len(string)

for i in range(length // 10):
    temp = string[:10]
    string = string[10:]
    print(temp)
print(string)
