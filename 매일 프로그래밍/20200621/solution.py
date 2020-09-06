# 정수 배열이 주어지면 , 배열 안의 모든 정수의 최대 공약수(GCD)를 구하시오.
# 시간 복잡도 제한 O(n)

def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def solution(arr):
    g = gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        g = gcd(g, arr[i])
    return g

a1 = [3, 2, 1] # 1
a2 = [2, 4, 6, 8] # 2
