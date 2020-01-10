# 출제의도는 모든 공백은 유지한 채로, 나타나는 단어의 앞 글자만 변경하는 것
def solution(s):
    answer = ''
    temp = s.lower().split(" ")
    
    for index in range(len(temp)):
        temp[index] = temp[index].capitalize()
        answer += temp[index] + " "    
    return answer[:-1]

# split(" ")가 아닌 split()를 그대로 사용하면 모든 공백이 지워짐
# capitalize()는 단어를 파라미터로 받아 첫문자만 처리하고 나머진 소문자 ex) 3people -> 3people
# title()은 문자열을 파라미터로 받아 나타나는 단어에서 첫번째 알파벳 문자를 바꿔주고 나머진 소문자 ex) 3people -> 3People