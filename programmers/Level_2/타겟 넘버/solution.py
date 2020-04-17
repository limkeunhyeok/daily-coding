def solution(numbers, target):
    answer = [0]
    for num in numbers:
        temp = []
        for n in answer:
            temp.append(n + num)
            temp.append(n - num)
        answer = temp
    return answer.count(target)

'''
다른 사람 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''