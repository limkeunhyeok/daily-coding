# 정수 배열과 타겟 숫자가 주어지면 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오
# 만약에 만족하는 두 원소의 인덱스가 여러 개일 경우 가장 먼저나오는 인덱스 쌍을 반환
# 만족하는 값이 없다면 -1
def solution(intArr, target):
    for idx, value in enumerate(intArr):
        try:
            answer = [idx, intArr.index(target - value)]
            return answer
        except ValueError:
            pass
    return -1
