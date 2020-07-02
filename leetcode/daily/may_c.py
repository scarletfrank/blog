from typing import List
import copy

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # directed graph, in-degree - out-degree = N - 1, judge
        count = [0] * (N + 1)
        for a, b in trust:
            count[a] -= 1 # out degree
            count[b] += 1 # in-degree
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        def helper(r, c):
            if image[r][c] == oldColor:
                image[r][c] = newColor
                if r >= 1: helper(r-1, c) # up
                if r+1 < m: helper(r+1, c) # down
                if c >= 1: helper(r, c-1) # left
                if c+1 < n: helper(r, c+1) # right
                # four direcions
        helper(sr, sc)
        return image
    # 单调栈？
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stk = []
        i = 0
        while i < len(num):
            while k > 0 and stk and stk[-1] > num[i]:
                stk.pop()
                k -= 1
            stk.append(num[i])
            i += 1
        while k > 0:
            stk.pop()
            k -= 1
        sb = [] # StringBuilder
        while stk:
            sb.append(stk.pop())
        sb = sb[::-1]
        while len(sb) > 1 and sb[0] == '0':
            sb = sb[1:]
        return "".join(sb)

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
# Prefix Tree /discuss/58989/My-python-solution
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True

res = Solution()
N = 2
trust = [[1, 2]]
image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc = 1, 1
newColor = 2
num = "10200"
k = 1
print(res.removeKdigits(num, k))
