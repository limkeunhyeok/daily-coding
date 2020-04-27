# 0과 1로 만들어진 2D 정수 배열이 있습니다. 0은 장애물이고 1은 도로일때,
#두 좌표가 주어지면, 첫번째 좌표에서 두번째 좌표까지 가장 가까운 거리를 구하시오.
# 두 좌표는 모두 도로에서 시작되고 좌, 우, 아래, 위로 움직이며 대각선으로는 움직일 수 없습니다.
#만약 갈 수 없다면 -1을 리턴하시오.
# Maze shortest path algorithm이라는 유명한 알고리즘 문제인 듯

from collections import deque

# Function annotation: 매개변수와 반환값을 명시적으로 보여준다.
# 배열 좌표를 저장
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

# BFS를 사용한 큐 데이터 구조
class queueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt
        self.dist = dist

# (row, col) 좌표의 유효성 체크        
def isValid(row: int, col: int, maxRow: int, maxCol: int):
    return (row >= 0) and (row < maxRow) and (col >= 0) and (col < maxCol)

# 최단거리를 찾는 함수
def BFS(matrix, src: Point, dest: Point):
    # 시작점과 도착점이 1이 아니라면 -1 반환
    if matrix[src.x][src.y] != 1 or matrix[dest.x][dest.y] != 1:
        return -1
    
    # 행과 열 최대값
    maxRow = len(matrix)
    maxCol = len(matrix[0])
    
    # 4가지 방향으로 이동을 위한 배열
    rowNum = [-1, 0, 0, 1] 
    colNum = [0, -1, 1, 0] 

    # 방문 여부 체크
    visited = [[False for i in range(maxCol)] for j in range(maxRow)]
    visited[src.x][src.y] = True

    # BFS를 위한 큐 생성
    q = deque()
    
    # 이동거리가 0인 시작 큐 노드 생성
    s = queueNode(src, 0)
    q.append(s)

    # 시작점에서 BFS 시작
    while q:
        curr = q.popleft()

        # 큐에서 꺼낸 노드가 도착점인지 체크
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist

        # 4가지 방향으로 좌표를 이동 
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # 이동한 좌표의 유효성 체크 및 큐에 삽입
            if (isValid(row, col, maxRow, maxCol) and matrix[row][col] == 1 and not visited[row][col]): 
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col), curr.dist + 1)
                q.append(Adjcell)
                
    # 도착점에 이르지 못하면 -1 반환
    return -1
        
def solution(matrix, start, finish):
    source = Point(start[0], start[1])
    dest = Point(finish[0], finish[1])
    return BFS(matrix, source, dest)