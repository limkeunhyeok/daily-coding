def comparison(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count >= 2:
        return False
    return True

def solution(begin, target, words):
	answer = [50]
	visited = [begin]
	if target not in words:
		return 0
	dfs(begin, target, words, 0, visited, answer)
	return answer[0]
	
def dfs(begin, target, words, count, visited, answer):
	if target == begin and count < answer[0]:
		answer[0] = count
		return
	for i in range(len(words)):
		if comparison(words[i], begin):
			if words[i] not in visited:				
				visited.append(words[i])
				dfs(words[i], target, words, count+1, visited, answer)
				visited.remove(words[i])