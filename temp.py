def solution(answers):
    answer = []
    Person1 = [1,2,3,4,5]
    Person2 = [2,1,2,3,2,4,2,5]
    Person3 = [3,3,1,1,2,2,4,4,5,5]
    Scores = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == Person1[i % 5]:
            Scores[0] += 1
        if answers[i] == Person2[i % 8]:
            Scores[1] += 1
        if answers[i] == Person3[i % 10]:
            Scores[2] += 1
    if Scores[0] == max(Scores):
        answer.append(1)
    if Scores[1] == max(Scores):
        answer.append(2)
    if Scores[2] == max(Scores):
        answer.append(3)
    return answer

answers = [1,2,3,4,5]
print(solution(answers))