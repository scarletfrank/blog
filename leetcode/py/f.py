from typing import List
import math

class Solution:
    # BackTrack
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        return all possible answers
        """
        ans = []
        empSol = [-1] * n
        # nums is a one-dimension array, like [1, 3, 0, 2] means
        # first queen is placed in column 1, second queen is placed
        # in column 3, etc.
        def solve(b, index, path, res):
            if index == len(b):
                res.append(path)
                return # backtrack
            for i in range(len(b)):
                b[index] = i
                if isValid(b, index):
                    tmp = "." * len(b)
                    solve(b, index + 1, path + [tmp[:i] + 'Q' + tmp[i+1:]], res)
        def isValid(b, n): # check whether n-th queen can be placed
            for i in range(n):
                if abs(b[i] - b[n]) == n - i or b[i] == b[n]: # diagonal and column check
                    return False
            return True
        solve(empSol, 0, [], ans)
        return ans

    # dp, and implicit dp
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            temp = dp[i-1] if dp[i-1] > 0 else 0
            dp.append(nums[i] + temp)
        return max(dp)
    def forkSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def totalNQueens(self, n: int) -> int:
        """
        return length of all possible answers
        """
        ans = []
        empSol = [-1] * n
        # nums is a one-dimension array, like [1, 3, 0, 2] means
        # first queen is placed in column 1, second queen is placed
        # in column 3, etc.
        def solve(b, index, path, res):
            if index == len(b):
                res.append(path)
                return # backtrack
            for i in range(len(b)):
                b[index] = i
                if isValid(b, index):
                    tmp = "." * len(b)
                    solve(b, index + 1, path + [tmp[:i] + 'Q' + tmp[i+1:]], res)
        def isValid(b, n): # check whether n-th queen can be placed
            for i in range(n):
                if abs(b[i] - b[n]) == n - i or b[i] == b[n]: # diagonal and column check
                    return False
            return True
        solve(empSol, 0, [], ans)
        return len(ans)
    # 触及边界的时候90°转向
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0]) # rows and columns
        occur = [[False] * n for _ in matrix]
        # 1 left 2 down 3 right 4 up
        offm = [0, 1, 0, -1]
        offn = [1, 0, -1, 0]
        i = j = di = 0 # start point and direction
        ary = []
        for _ in range(m*n):
            ary.append(matrix[i][j])
            occur[i][j] = True
            ni, nj = i + offm[di], j + offn[di]
            if 0 <= ni < m and 0 <= nj < n and not occur[ni][nj]:
                i, j = ni, nj
            else:
                di = (di + 1) % 4
                i, j = i + offm[di], j + offn[di]
        return ary

    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if lastPos <= nums[i] + i:
                lastPos = i
        return lastPos == 0

    # fork
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        key = newInterval[0]
        # Insertion
        n = len(intervals) - 1 # 有序区的最后一个元素
        intervals.append(newInterval) # append at last
        while n >= 0 and intervals[n][0] > key:
            intervals[n+1] = intervals[n]
            n = n - 1
        intervals[n+1] = newInterval
        # Merge, and sorted by x[0] alreadyi
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        a = b = n
        occur = [[False] * n for _ in range(n)]
        # 1 left 2 down 3 right 4 up
        offm = [0, 1, 0, -1]
        offn = [1, 0, -1, 0]
        i = j = di = 0 # start point and direction
        ans = [[0] * n for _ in range(n)]
        for _ in range(a*b):
            ans[i][j] = _ + 1
            occur[i][j] = True
            ni, nj = i + offm[di], j + offn[di]
            if 0 <= ni < a and 0 <= nj < b and not occur[ni][nj]:
                i, j = ni, nj
            else:
                di = (di + 1) % 4
                i, j = i + offm[di], j + offn[di]
        return ans

    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(nums[index])
            nums.remove(nums[index])
        return permutation


