from typing import List
from collections import defaultdict
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, r, path):
            if not nums: # len(p) = len(n)
                r.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], r, path + [nums[i]])
        res = []
        dfs(nums, res, [])
        return res
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            bag=[0] * 26
            for c in s:
                bag[ord(c) - ord('a')] += 1
            d[tuple(bag)].append(s)
        return d.values()
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / myPow(x, -n)
        if n % 2: # n is odd
            return x * myPow(x, n - 1)
        return myPow(x * x, n / 2)

# 2.00000 -2147483648
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
b = [1,1,2]
c = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
res = Solution()
#print(res.permute(a))
#print(res.permuteUnique(b))
ans = res.groupAnagrams(a)
print(ans)