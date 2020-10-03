def solution(files):
    pattern = list(files.pop(0))
    for i in range(len(files)):
        for j in range(len(pattern)):
            if pattern[j] == files[i][j]:
                continue
            else:
                pattern[j] = '?'
    answer = ''.join(pattern)
    return answer

N = int(input())
files = []
for _ in range(N):
    file = input()
    files.append(file)
print(solution(files))