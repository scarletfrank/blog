# note 1
# https://docs.python.org/3/library/typing.html
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force => Time Limit Exceeded
        # One-pass Hash Table
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if str(complement) in d:
                return [d.get(str(complement)), i]
            d[str(nums[i])] = i
    # Linked-list
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p, q, current = l1, l2, dummyHead
        c = 0 # carry
        while (p != None or q != None):
            a = p.val if p != None else 0
            b = q.val if q != None else 0
            m = a + b + c
            c = m // 10
            current.next = ListNode(m % 10)
            current = current.next
            if p != None: p = p.next
            if q != None: q = q.next 
        if c > 0:
            current.next = ListNode(c)
        return dummyHead.next
    # Set
    def lengthOfLS(self, s: str) -> int:
        d = set()
        n = len(s)
        l, i, j = 0, 0, 0
        while (i < n and j < n):
            if s[j] not in d:
                d.add(s[j])
                j = j + 1
                l = j - i if (j - i) > l else l
            else:
                d.remove(s[i])
                i = i + 1
        return l
    # Dict
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, l = len(s), 0
        d = {}
        i, j = 0, 0
        for j in range(n):
            if s[j] in d:
                i = max(d[s[j]], i)
            l = max(l, j - i + 1)
            d[s[j]] = j + 1
        return l
    # Binary Search
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: # ensure m <= n
            nums1, nums2, m, n = nums2, nums1, n, m # swap
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, (m + n + 1) // 2 
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < imax and nums2[j - 1] > nums1[i]:
                imin = i + 1 # i is too small
            elif i > imin and nums1[i - 1] > nums2[j]:
                imax = i - 1 # i is too big
            else: 
                # i is perfect
                if i == 0: max_left = nums2[j - 1]
                elif j == 0: max_left = nums1[i - 1]
                else: max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1: 
                    return max_left

                if i == m: min_right = nums2[j]
                elif j == n: min_right = nums1[i]
                else: min_right = min(nums2[j], nums1[i])

                return (max_left + min_right) / 2.0
    def longestPalindrome(self, s: str) -> str:
        """ TBD 
        1. Longest Common Substring: Dynamic Programming 
        2. Brute Force: d[::-1]
        3. Dynamic Programming
        4. Expand Around Center: 2n - 1 centers
        """
        def expandAroundCenter(d: str, left: int, right: int):
            l, r = left, right
            while(l >= 0 and r < len(d) and s[l] == s[r]):
                l, r = l - 1, r + 1
            return r - l - 1
        if s == "" or len(s) < 1: return ""
        start, end = 0, 0  
        n = len(s)
        for i in range(n):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > (end - start):
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start : end + 1]
    # ZigZag Conversion
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * min(numRows, len(s)) # non-empty rows of the Zig-Zag Pattern
        curRow, goingDown = 0, False
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = bool(1 - goingDown) # Zig-Zag Characteristic
            curRow += 1 if goingDown else -1
        ret = ""
        for row in rows:
            ret += row
        return ret
    # Reverse Integer
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        # zero check
        l = []
        if x < 0:
            l.append("-")
            x = x * -1
        while x != 0:
            t = x % 10
            x = x // 10
            l.append(t)
        flag, y = 0, 0
        for e in l:
            if e == '-':
                flag = 1
                continue
            else:
                y = y * 10
                y = y + e
        y = y if flag == 0 else -1 * y
        # sign check
        # overflow check
        if y <= 2 ** 31 - 1 and y >= -2 ** 31: 
            return y
        else:
            return 0
    def APIreverse(self, x: int) -> int:
        if x == 0:
            return 0
        # zero check
        s = str(x)[::-1]
        y = int(s) if x >= 0 else int(s[:-1]) * -1
        # sign check
        # overflow check
        if y <= 2 ** 31 - 1 and y >= -2 ** 31: 
            return y
        else:
            return 0
    def myAtoi(self, s: str) -> int:
        s = s.rstrip().lstrip() # whitespace
        flag = 0
        if len(s) == 0:
            return 0
        if s[0] == '-':
            flag = 1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        elif s[0].isdigit() == False:
            return 0 # no valid conversion could be performed
        i = ""
        for c in s:
            if c.isdigit():
                i = i + c
            else:
                break
        y = 0
        for e in i:
            y = y * 10
            y = y + (ord(e) - ord('0'))
        y = y if flag == 0 else -1 * y
        if y > 2 ** 31 - 1:
            y = 2 ** 31 -1
        elif y < -2 ** 31:
            y = -2 ** 31
        else:
            return y # default case
        return y
    def APImyAtoi(self, s: str) -> int:
        s = s.rstrip().lstrip() # whitespace
        flag = 0
        if len(s) == 0:
            return 0
        if s[0] == '-':
            flag = 1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        elif s[0].isdigit() == False:
            return 0 # no valid conversion could be performed
        i = "" 
        for c in s:
            if c.isdigit():
                i = i + c
            else:
                break
        if len(i) == 0: # no valid number
            return 0
        x = int (i) * -1 if flag else int(i) 
        if x > 2 ** 31 - 1:
            x = 2 ** 31 -1
        elif x < -2 ** 31:
            x = -2 ** 31
        else:
            return x # default case
        return x
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = []
        z = x
        while z != 0:
            t = z % 10
            z = z // 10
            l.append(t)
        y = 0
        for e in l:
            y = y * 10
            y = y + e
        return y == x
    def APIisPalindrome(self, x: int) -> bool:
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False
    # Regular Expression Matching
    # Recursion & Dynamic Programming
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
    # Regular Expression is different with Wildcard in BASH
        