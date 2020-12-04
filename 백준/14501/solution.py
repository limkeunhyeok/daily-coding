def solution(n, time, pay):
    dp = pay
    dp.append(0)
    for i in range(n - 1, -1, -1):
        if time[i] + i > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], pay[i] + dp[i + time[i]])
    return dp[0]

time = []
pay = []
n = int(input())
for _ in range(n):
    t, p = map(int, input().split(' '))
    time.append(t)
    pay.append(p)

print(solution(n, time, pay))

n1 = 7
t1 = [3, 5, 1, 1, 2, 4, 2]
p1 = [10, 20, 10, 20, 15, 40, 200] # 45

n2 = 10
t2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
p2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 55

n3 = 10
t3 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
p3 = [10, 9, 8, 7, 6, 10, 9, 8, 7, 6] # 20

n4 = 10
t4 = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
p4 = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50] # 90