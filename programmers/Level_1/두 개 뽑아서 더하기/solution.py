def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        answer += [numbers[i] + j for j in numbers[i + 1:]]
    
    answer = sorted(list(set(answer)))
    return answer