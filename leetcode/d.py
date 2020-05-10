from typing import List
import math

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        本来还想从逆序数来做的
        """
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]: # find a[i-1]
            i = i - 1
        if i >= 0: # find a[j]
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j = j - 1
            # swap nums i j
            nums[i], nums[j] = nums[j], nums[i]
        # reverse(nums, i + 1)
        start, j = i + 1, len(nums) - 1
        while start < j:
            nums[start], nums[j] = nums[j], nums[start]
            start, j = start + 1, j - 1       
    # Hard
    def longestValidParentheses(self, s: str) -> int:
        m ={'(':')', '}':'{', ']':'['}
        stack, cnt = [-1], 0
        longest = 0
        for i in range(len(s)):
            if s[i] in m:
                stack.append(i)
            else:
                stack.pop() 
                if len(stack) == 0:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])
        return longest
    # Search in Rotated Sorted Array, 联动 81
    # If nums[mid] and target are "on the same side" of nums[0], just take nums[mid]
    # [solution](http://bangbingsyb.blogspot.com/2014/11/leetcode-search-in-rotated-sorted-array.html)
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < nums[r]: # right half sorted
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:                 # left half sorted
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1 
        return -1
    # Find First and Last Position of Element in Sorted Array
    # Great Similar Question: https://leetcode.com/problems/first-bad-version/ 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(nums, target, left):      
            l, r = 0, len(nums)
            start, end = 0, 0
            while l < r:
                m = (l + r) // 2
                if nums[m] > target or (left and target == nums[m]): # variable left controls a condition
                    r = m
                else:
                    l = m + 1
            return l
        left_idx = bs(nums, target, True) # find left most index
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, bs(nums, target, False) - 1] # find right most index

            
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            else:
                pass
        return len(nums) # if all pass
    # Binary Variant
    def BSsearchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return i
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def dup(ary):
            d = {}
            for a in ary:
                if a == '.':
                    continue
                if a in d:
                    return True
                else:
                    d[a]= 1
            return False
        # first-pass, row check
        rows = [dup(row) for row in board]
        if True in rows:
            return False
        # second-pass, column check
        t = []
        for i in range(9):
            col = [row[i] for row in board]
            if dup(col) == True:
                return False
        # third-pass, sub-boxex check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub = [row[j:j+3] for row in board[i:i+3]]
                sub1 = []
                for s in sub:
                    sub1 += s
                if dup(sub1) == True:
                    return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve(b: List[List[str]]):
            for i in range(9):
                for j in range(9):
                    if b[i][j] == '.':
                        for c in range(1, 10):
                            if isValid(b, i, j, str(c)):
                                board[i][j] = str(c) # put c for this cell
                                if solve(b):
                                    return True # Solution get
                                else:
                                    board[i][j] = '.' # backtrack
                        return False
            return True

        def isValid(b: List[List[str]], row: int, col: int, c: str):
            regionRow = 3 * (row // 3)
            regionCol = 3 * (col // 3)
            for i in range(9):
                if b[i][col] == c or b[row][i] == c or board[regionRow + i // 3][regionCol + i % 3] == c:
                    return False
            return True
        if board == None or len(board) == 0:
            return
        solve(board)
    def DFSsolveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def validate(b: List[List[str]], i: int, j: int, flag: List[bool]):
            for k in range(9):
                if b[i][k] != '.':
                    flag[int(b[i][k])] = False
                if b[k][j] != '.':
                    flag[int(b[k][j])] = False
                r = i // 3 * 3 + k // 3
                c = j // 3 * 3 + k % 3
                if b[r][c] != '.':
                    flag[int(b[r][c])] = False
        def dfs(b: List[List[str]], d: int):
            if d == 81:
                return True
            i, j = d // 9, d % 9
            if b[i][j] != '.':
                return dfs(b, d + 1)  # prefill number skip
            flag = [True] * 10
            validate(b, i, j, flag)
            for k in range(1, 10):
                if flag[k]:
                    b[i][j] = str(k)
                    if dfs(b, d + 1): return True
            b[i][j] = '.'
            return False
        dfs(board, 0)
    # Key: 如果下一个字符跟当前一致，则是 two xxx，不一致则为 one xxx
    def countAndSay(self, n: int) -> str:
        s = '1' # base case
        for i in range(n-1):
            cnt, temp = 1, []
            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    cnt = cnt + 1
                else:
                    temp.append(str(cnt))
                    temp.append(s[j - 1]) 
                    cnt = 1
            temp.append(str(cnt))
            temp.append(s[-1])
            s = ''.join(temp)
        return s
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def solve(c: List[int], t: int, tempList: List[int], start: int, a: List[List[int]]):
            # t: remain
            if t < 0:
                return
            elif t == 0:
                ans.append(tempList)
            else:
                for i in range(start, len(c)):
                    solve(c, t - c[i], tempList + [c[i]], i, a) # success if return here

        solve(candidates, target, [], 0, ans)
        return ans
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # used once, so modify start 
        ans = []
        candidates.sort()
        def solve(c: List[int], t: int, tempList: List[int], start: int, a: List[List[int]]):
            # t: remain
            if t < 0:
                return
            elif t == 0:
                ans.append(tempList)
            else:
                for i in range(start, len(c)):
                    if i > start and c[i] == c[i - 1]: # skip 2nd duplicate element
                        continue
                    if c[i] > t: # if bigger, no need to backtrack
                        break
                     solve(c, t - c[i], tempList + [c[i]], i + 1, a) # success if return here
        solve(candidates, target, [], 0, ans)
        return ans 
