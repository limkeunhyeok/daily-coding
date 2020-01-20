# 정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오.
# 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다.
# 단, 정수를 문자열로 바꾸면 안됩니다.
def solution(n):
    if n < 0:
        return False
    temp = []
    
    while n != 0:
        temp.append(n % 10)
        n = n // 10
    
    for i in range(len(temp) // 2):
        if temp[i] != temp[len(temp) - i - 1]:
            return False
    return True