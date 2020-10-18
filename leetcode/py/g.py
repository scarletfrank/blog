# note 1
# https://docs.python.org/3/library/typing.html
from typing import List
import re

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # similar 189. Rotate Array
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        current = dummyHead = ListNode(0)
        q = head
        ary = []
        while q != None:
            ary.append(q.val)
            q = q.next
        n = len(ary)
        if n == 0 or n == 1:
            return head
        k = k % n
        for c in ary[n-k:] + ary[:n-k]:
            current.next = ListNode(c)
            current = current.next
        return dummyHead.next
    # m x n grid, m columns, n rows
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * m 
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(m):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j-1]
        return dp[m-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        elif m == 1:
            return sum(grid[0])
        else:
            n = len(grid[0])
        # first Row
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        # first Column
        for j in range(1, m):
            grid[j][0] += grid[j-1][0]
        # update the rest grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]
    # Regular Expression for decimal number
    #  "[+-]?[0-9]+(.[0-9]+)?(e[+-]?[0-9]+)?"
    # edge case: .1 
    # fork DFA, best solution from my point of view
    def isNumber(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        #define DFA state transition tables
        states = [{},
                 # State (1) - initial state (scan ahead thru blanks)
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4},
                 # State (2) - found sign (expect digit/dot)
                 {'digit':3, '.':4},
                 # State (3) - digit consumer (loop until non-digit)
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 # State (4) - found dot (only a digit is valid)
                 {'digit':5},
                 # State (5) - after dot (expect digits, e, or end of valid input)
                 {'digit':5, 'e':6, 'blank':9},
                 # State (6) - found 'e' (only a sign or digit valid)
                 {'sign':7, 'digit':8},
                 # State (7) - sign after 'e' (only digit)
                 {'digit':8},
                 # State (8) - digit after 'e' (expect digits or end of valid input) 
                 {'digit':8, 'blank':9},
                 # State (9) - Terminal state (fail if non-blank found)
                 {'blank':9}]
        currentState = 1
        for c in s:
            # If char c is of a known class set it to the class name
            if c in '0123456789':
                c = 'digit'
            elif c in ' \t\n':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            # State transition
            currentState = states[currentState][c]
        # The only valid terminal states are end on digit, after dot, digit after e, or white space after valid input    
        if currentState not in [3,5,8,9]:
            return False
        return True

    def plusOne(self, digits: List[int]) -> List[int]:
        i, j = 0, len(digits) - 1
        c = 1 # carry = 0
        ary = []
        while c != 0:
            if j == len(digits) - 1:
                t = digits[j] + 1 + c - 1 # cuz c = 1 initially
            elif j == -1: # edge case
                t = c
            else:
                t = digits[j] + c
            a, b = t % 10, t // 10
            ary.append(a)
            j = j - 1
            c = b
        for k in range(j, -1, -1):
            ary.append(digits[k])
        # ary[::-1]
        return ary[::-1]

    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        c = 1 # initial carry = 0, but for convenience of loop control
        ary = []
        while i != -1 or j != -1:
            if i == len(a) - 1 and j == len(b) - 1:
                c = 0
            m = ord(a[i]) - ord('0') if i != -1 else 0
            n = ord(b[j]) - ord('0') if j != -1 else 0
            t = m + n + c
            d, e = t % 2, t // 2
            ary.append(str(d))
            c = e
            if i != -1: # for i reachs the end, 0
                i = i - 1
            if j != -1:
                j = j - 1
        if c > 0:
            ary.append(str(c))
        return "".join(ary[::-1])
        
    def mySqrt(self, x: int) -> int:
        a, b = 0, x
        if x == 1:
            return 1
        while a < b:
            m = (a + b) // 2
            if m * m == x:
                return m
            elif m * m > x:
                b = m - 1
            else:
                if (m+1)*(m+1) > x:
                    return m
                else:
                    a = m + 1
        return a