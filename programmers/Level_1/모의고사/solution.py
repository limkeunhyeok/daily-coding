def check(person, answers):
    patten = len(person)
    count = 0
    for i in range(len(answers)):
        if answers[i] == person[i%patten]:
            count += 1
    return count

def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    scores = []
    scores.append(check(person1, answers))
    scores.append(check(person2, answers))
    scores.append(check(person3, answers))
    
    if scores[0] == max(scores):
        answer.append(1)
    if scores[1] == max(scores):
        answer.append(2)
    if scores[2] == max(scores):
        answer.append(3)
    return answer