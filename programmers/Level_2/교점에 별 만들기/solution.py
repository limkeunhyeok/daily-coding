def isCross(line1, line2):
    A, B, E = line1
    C, D, F = line2
    if ((A * D) - (B * C)) == 0:
        return False
    return True

def getCrossPoint(line1, line2):
    A, B, E = line1
    C, D, F = line2
    x = ((B * F) - (E * D)) / ((A * D) - (B * C))
    y = ((E * C) - (A * F)) / ((A * D) - (B * C))
    return [x, y]

def getCorrectCrossPoint(points):
    answer = []
    for point in points:
        x, y = point
        if int(x) == x and int(y) == y:
            answer.append([int(x), int(y)])
    return answer

def getAllCrossPoint(line):
    crossPoints = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if isCross(line[i], line[j]):
                crossPoint = getCrossPoint(line[i], line[j])
                crossPoints.append(crossPoint)
    return getCorrectCrossPoint(crossPoints)

def getMinAndMaxPoint(points):
    xPos = []
    yPos = []
    for point in points:
        xPos.append(point[0])
        yPos.append(point[1])
    xMin, xMax = min(xPos), max(xPos)
    yMin, yMax = min(yPos), max(yPos)
    return xMin, xMax, yMin, yMax


def solution(line):
    answer = []
    crossPoints = getAllCrossPoint(line)
    xMin, xMax, yMin, yMax = getMinAndMaxPoint(crossPoints)
    answer = ["." * (xMax - xMin + 1)] * (yMax - yMin + 1)
    for point in crossPoints:
        x, y = point
        answer[yMax - y] = answer[yMax - y][:x - xMin] + "*" + answer[yMax - y][x - xMin + 1:]
    return [''.join(ans) for ans in answer]