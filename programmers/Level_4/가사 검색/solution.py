from collections import defaultdict

class Node(object):
    def __init__(self, key, data=None, length=None):
        self.key = key
        self.data = data
        self.children = {}
        self.length = defaultdict(int)

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current = self.head
        current.length[len(string)] += 1

        for c in string:
            if c not in current.children:
                current.children[c] = Node(c)
            current.children[c].length[len(string)] += 1
            current = current.children[c]
        current.data = string
  
    def starts_with(self, prefix, length):
        current = self.head
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return 0
        return current.length[length]

def solution(words, queries):
    answer = []
    front = Trie()
    back = Trie()

    for word in words:
        front.insert(word)
        back.insert(word[::-1])
    
    for word in queries:
        if word == "?" * len(word):
            answer.append(front.head.length[len(word)])
        elif word[0] == "?":
            prefix = word[::-1].replace('?', '')
            answer.append(back.starts_with(prefix, len(word)))
        else:
            prefix = word.replace('?', '')
            answer.append(front.starts_with(prefix, len(word)))
    return answer
    