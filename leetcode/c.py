import math
from queue import PriorityQueue
from collections import Counter, defaultdict
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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
    def mergeTwoLists(self, l1: ListNode, l2:ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p, q, current = l1, l2, dummyHead
        while p != None and q != None:
            if p.val < q.val:
                current.next = ListNode(p.val)
                p = p.next
                current = current.next
            else:
                current.next = ListNode(q.val)
                q = q.next
                current = current.next      
        if q != None: p = q
        while p != None:
            current.next = ListNode(p.val) 
            p = p.next
            current = current.next
        return dummyHead.next
    # TBD asymptotically analysis
    # Catalan number
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
        backtrack()
        return ans
    # BruteForce
    def BFmergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
    # Compare one by one, TLE case: large 1-node lists
    def TBDmergeKLists(self, lists: List[ListNode]) -> ListNode:
        cur = dummyHead = ListNode(0)
        while True:
            cnt = True
            min_index, curmin = 0, math.inf
            for i in range(len(lists)):
                if lists[i] != None:
                    if lists[i].val < curmin:
                        min_index, curmin = i, lists[i].val
                    cnt = False
            if cnt:
                break
            cur.next = ListNode(curmin)
            cur = cur.next
            lists[min_index] = lists[min_index].next
        return dummyHead.next
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        cur = dummyHead = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().node
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return dummyHead.next
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        second = head.next
        pre = ListNode(0)
        while head and head.next:
            nxt = head.next
            head.next = nxt.next # 连接最远的节点
            nxt.next = head # 交换邻接节点
            pre.next = nxt # 连接“previous”的头
            head = head.next # 下一个
            pre = nxt.next # 替换“previous”
        return second
    # Recursion
    def IswapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        head = cur.next
        cur.next = self.swapPairs(head.next)
        head.next = cur
        return head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n, cur = 0, head
        dummyHead = ListNode(0)
        dummyHead.next = head
        while cur != None:
            n = n + 1
            cur = cur.next
        prev, tail = dummyHead, head
        while n >= k:
            for i in range(1, k):
                next = tail.next.next
                tail.next.next = prev.next
                prev.next = tail.next
                tail.next = next
            prev = tail
            tail = tail.next
            n = n - k
        return dummyHead.next


    def removeDuplicates(self, nums: List[int]) -> int:
        # return the length
        # Different Algorithm for a linked-list
        if len(nums) == 0: return 0
        n, cur = len(nums), 0
        for i in range(1, n):
            if nums[i] != nums[cur]:
                cur = cur + 1
                nums[cur] = nums[i]
        return cur + 1 
    def removeElement(self, nums: List[int], val: int) -> int:
        # return length
        if len(nums) == 0: return 0
        n, cur = len(nums), 0
        for i in range(n):
            if nums[i] != val:
                nums[cur] = nums[i]
                cur = cur + 1
        return cur 

    def strStr(self, haystack: str, needle: str) -> int:
        # KMP or find()
        if len(needle) == 0: return 0 # emtpy pattern
        n = len(needle)
        j, k = 0, -1
        nextv = [-1] * n
        while j < n - 1:
            if k == -1 or needle[j] == needle[k]:
                j, k = j + 1, k + 1
                nextv[j] = k
            else:
                k = nextv[k]
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = nextv[j]
        if j == len(needle):
            return i - j
        else:
            return -1
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1 if (dividend < 0) ^ (divisor < 0) else 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            c = divisor
            i = 0
            while (c << i) <= dividend:
                dividend -= (c << i)
                res += (1 << i)
                i = i + 1
        if flag: res = -res
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return int(res)
    # [doc](https://docs.python.org/3.8/library/collections.html#collections.defaultdict)
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordBag = Counter(words)
        if len(words) == 0: return []
        wordLen, numWords = len(words[0]), len(words)
        totalLen, res = wordLen * numWords, []
        for i in range(len(s) - totalLen + 1):
            seen = defaultdict(int) 
            for j in range(i, i + totalLen, wordLen):
                currWord = s[j: j + wordLen]
                if currWord in wordBag:
                    seen[currWord] += 1
                    if seen[currWord] > wordBag[currWord]:
                        break
                else:
                    break
            if seen == wordBag:
                res.append(i)
        return res
        

