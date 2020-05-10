from typing import List
from itertools import product
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Container With Most Water
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i, j = 0, len(height) - 1
        while i < j:
            maxarea = max(maxarea, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return maxarea   
    def intToRoman(self, num: int) -> str:
        r_nums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L',
                'XL', 'X', 'IX', 'V', 'IV', 'I']
        a_nums = [1000, 900, 500, 400, 100, 90, 
                    50,   40,  10,  9,   5,   4, 1]
        roman, remainder = "", int(num)
        for i in range(len(r_nums)):
            while remainder >= a_nums[i]:
                roman = roman + r_nums[i]
                remainder = remainder - a_nums[i]
            if remainder <= 0: break
        return roman
    def romanToInt(self, s: str) -> int:
        r_nums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L',
                'XL', 'X', 'IX', 'V', 'IV', 'I']
        a_nums = [1000, 900, 500, 400, 100,
                    90, 50, 40, 10, 9, 5, 4, 1]
        remainder = s
        arabic = 0
        for i in range(len(r_nums)):
            numchr = len(r_nums[i])
            while remainder[:numchr] == r_nums[i]:
                arabic += a_nums[i]
                remainder = remainder[numchr :]
                #print(remainder, a_nums[i])
            if len(remainder) <= 0: break
        if arabic > 0 and arabic < 4000: return arabic

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        p = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(p) != 0:
                p = p[:-1]
                if len(p) == 0: return ""
        return p
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip this round
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r = r - 1
                elif s < 0:
                    l = l + 1
                else: # s == 0
                    ans.append((nums[i], nums[l], nums[r]))
                    # remove duplicates
                    while l < r and nums[l] == nums[l+1]: l+=1
                    while l < r and nums[r] == nums[r-1]: r-= 1
                    l += 1
                    r -= 1
        return ans
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0]+nums[1]+nums[2]
        diff = abs(closest - target)
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                newDiff = abs(s - target)
                if diff > newDiff:
                    diff, closest = newDiff, s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return closest
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'1': "", '2': "a b c", '3': "d e f", '4': "g h i", '5': "j k l",
             '6': "m n o", '7': "p q r s", '8': "t u v", '9': "w x y z"}
        letters = []
        if digits == "":
            return []
        for digit in digits:
            if d[digit] == "": continue
            letters.append(d[digit].split())
        ans = []
        for x in product(*letters):
            ans.append(''.join(x))
        return ans
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(nums: List[int], t: int) -> List[List[int]]:
            ans = []
            nums.sort()
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue # skip this round
                l, r = i + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s > t:
                        r = r - 1
                    elif s < t:
                        l = l + 1
                    else: # s == 0
                        ans.append((nums[i], nums[l], nums[r]))
                        # remove duplicates
                        while l < r and nums[l] == nums[l+1]: l+=1
                        while l < r and nums[r] == nums[r-1]: r-= 1
                        l += 1
                        r -= 1
            return ans
        ans = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sub = target - nums[i]
            sols = threeSum(nums[i+1:], sub)
            if len(sols) is not 0:
                for s in sols:
                    ans.append([nums[i]] + list(s))
        return ans
    # 24ms 95.62%
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h, cnt = head, 0
        while h != None:
            cnt += 1
            h = h.next
        sub = cnt - n
        cur, cnt = head, 0
        while cur != None:
            if cnt == sub - 1: # normal case
                cur.next = cur.next.next
                # skip node
            elif sub == 0: # remove 1st element
                return head.next
            cnt += 1
            cur = cur.next
        return head
    # valid parentheses: stack
    def isValid(self, s: str) -> bool:
        m ={')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in m:
                n = stack.pop() if stack else '#' # essential, in case of error of poping from empty list
                if n != m[c]:
                    return False
            else:
                stack.append(c)
        if stack == []:
            return True
        else:
            return False
        

        

        