# "./"과 "../" 이 포함된 파일 경로를 "./"과 "../"이 없는 유닉스 파일 경로로 바꾸시오.
# "./"는 현재의 위치를 뜻하고, "../"는 상위 디렉토리를 뜻합니다.

def solution(path):
    answer = '/'
    temp = []
    splitted = path.split('/')
    
    for p in splitted:
        if p == '' or p == '.':
            continue
        elif p == '..':
            temp.pop(-1)
        else:
            temp.append(p)
    
    for p in temp:
        answer += p + '/'
    return answer