from typing import List
from collections import defaultdict
class Solution:
    # smallest missing positive integer
    # Theta (n) constant extra space
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < n and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    ans = ans + (left_max - height[l])
                l = l + 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    ans = ans + (right_max - height[r])
                r = r - 1
        return ans
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        pos = [0] * (m+n)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                Sum = mul + pos[i+j+1]
                pos[i+j] = pos[i+j] + (Sum//10)
                pos[i+j+1] = Sum % 10
        res = []
        for p in pos:
            if p != 0 or len(res) != 0:
                res.append(str(p))
        if len(res) == 0:
            return "0"
        else:
            return "".join(res)

    # DP solution & FSM solution
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for i in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = False
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1] == '?')
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[m][n]
        
    def FSMisMatch(self, s: str, p: str) -> bool:
        transfer, state = {}, 0
        for char in p:
            if char == '*':
                tranfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1
        accept = state # 接受状态
        states = set([0]) # 开始状态
        for char in s:
            states = set([transfer.get((at, token)) for at in states for token in [char, '*', '?']])
        return accept in states

    # Jump Game Two
    # BFS or Greedy ? Greedy strategy can be used in Jump Game too
    def jump(self, nums: List[int]) -> int:
        end, maxPosition, steps = 0, 0, 0
        for i in range(len(nums) - 1):
            maxPosition = max(maxPosition, nums[i] + i)
            if maxPosition == len(nums) - 1:
                return True
            if i == end:
                end = maxPosition
                steps += 1
        return steps
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, r, path):
            if not nums: # len(p) = len(n)
                r.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], r, path + [nums[i]])
        res = []
        dfs(nums, res, [])
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, r, path):
            if not nums: # len(p) = len(n)
                r.append(path)
            for i in range(len(nums)):
                if i != 0 and num[i-1] == num[i]:
                    continue
                dfs(nums[:i] + nums[i+1:], r, path + [nums[i]])
        res = []
        dfs(nums, res, [])
        return res

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            bag=[0] * 26
            for c in s:
                bag[ord(c) - ord(a)] += 1
            d[tuple(bag)].append(s)
        return d.values
    # Recursion
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / myPow(x, -n)
        if n % 2: # n is odd
            return x * myPow(x, n - 1)
        return myPow(x * x, n / 2)
    # Iterative
    def ImyPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1/x, -n
        base = 1
        while n:
            if n & 1: # if n % 2 , n is odd
                base *= x
            x *= x
            n >>= 1
        return base


