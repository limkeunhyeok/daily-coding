def solution(n, k):
    answer = []
    k -= 1
    factorial = [1]
    people = [i + 1 for i in range(n)]
    for i in range(2, n):
        factorial.append(factorial[-1] * i)
        
    for i in range(n - 1):
        if k == 0:
            answer += people
            return answer
        d, m = divmod(k, factorial[-1])
        answer.append(people.pop(d))
        k = m
        factorial.pop(-1)
    return answer + people