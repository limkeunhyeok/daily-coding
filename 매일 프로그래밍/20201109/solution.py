"""
answer = []

def permute(s, ele):
    global answer
    if len(s) == 1:
        ele += s
        answer.append(ele)
    else:
        for i in range(len(s)):
            newEle = ele + s[i]
            subString = s[:i] + s[i + 1:]
            permute(subString, newEle)

def solution(s):
    global answer
    permute(s, '')
    print(*answer)
"""
def toString(List): 
	return ''.join(List) 

def permute(a, l, r): 
	if l==r: 
		print(toString(a)) 
	else: 
		for i in range(l,r+1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l] # backtrack 

string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 
