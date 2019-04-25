num = input("숫자 입력 : ")
temp = list(num) # 문자열을 리스트로 변환
temp = [int (i) for i in temp] # 리스트 문자열 int형으로 변환
answer = []
result = ''
answer.append(str(temp[0]))

for i in range(len(temp) - 1):
    if(temp[i] % 2 == 0 and temp[i + 1] % 2 == 0):
        answer.append('*')
        answer.append(str(temp[i + 1]))
    elif(temp[i] % 2 == 1 and temp[i + 1] % 2 == 1):
        answer.append('-')
        answer.append(str(temp[i + 1]))
    else:
        answer.append(str(temp[i + 1]))

for i in answer:
    result += i