def grading(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 50 and score < 70:
        return "D"
    else:
        return "F"

def getAverage(index, score):
    answer = 0
    length = len(score)
    minScore = min(score)
    maxScore = max(score)
    total = sum(score)
    
    if score[index] == minScore and score.count(minScore) == 1:
        total -= minScore
        length -= 1
    elif score[index] == maxScore and score.count(maxScore) == 1:
        total -= maxScore
        length -= 1
        
    answer = total / length
    return answer

def matchScores(scores):
    answer = [[] for i in range(len(scores))]
    
    for i in range(len(scores)):
        for j in range(len(scores)):
            answer[j].append(scores[i][j])
    return answer

def solution(scores):
    answer = ''
    newScores = matchScores(scores)
    for index, score in enumerate(newScores):
        average = getAverage(index, score)
        grade = grading(average)
        answer += grade
    return answer