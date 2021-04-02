answer = [0, 1, 2, 4]
for i in range(3, 11):
    answer.append(sum(answer[i - 2 : i + 1]))
    
for _ in range(int(input())):
    print(answer[int(input())])
