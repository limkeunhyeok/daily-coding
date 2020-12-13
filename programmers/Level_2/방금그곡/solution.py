def calcTime(start, end):
    startHour, startMin = map(int, start.split(':'))
    endHour, endMin = map(int, end.split(':'))
    answer = endMin - startMin
    answer += 60 * (endHour - startHour)
    return answer

def replaceCode(melody):
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    melody = melody.replace('A#', 'a')    
    return melody 

def played(code, time):
    answer = ''
    l = len(code)
    for i in range(time):
        temp = i % l
        answer += code[temp]
    return answer

def solution(m, musicinfos):
    answer = []
    m = replaceCode(m)
    for i in range(len(musicinfos)):
        start, end, title, code = musicinfos[i].split(',')
        time = calcTime(start, end)
        code = replaceCode(code)
        melody = played(code, time)
        if m in melody:
            answer.append([i, time, title])

    if not answer:
        return "(None)"
    answer = sorted(answer, key = lambda x: (-x[1], x[0]))
    return answer[0][2]