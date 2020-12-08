from typing import List
from listnode import ListNode

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
            
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        O(n) time
        O(n) space => TBD O(1) space
        """
        dummyHead = ListNode(0)
        p, q = head, dummyHead
        while p is not None:
            v = p.val
            if v == val:
                p = p.next
                continue # skip it
            # Non-skip case
            q.next = ListNode(v)
            q = q.next
            p = p.next
        return dummyHead.next
    
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        mark = [True for _ in range(n)]
        mark[0] = mark[1] = False
        for i in range(2, int(n ** 0.5) + 1): # 从2开始
            if mark[i]:
                for j in range(i*i, n, i):
                    mark[j] = False
        return sum(mark) # 
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s and t have the same length
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
        # m1, m2 = [0 for _ in range(256)], [0 for _ in range(256)]
        # for i in range(len(s)):
        #     if m1[ord(s[i])] != m2[ord(t[i])]:
        #         return False
        #     m1[ord(s[i])] = i + 1
        #     m2[ord(t[i])] = i + 1
        # return True