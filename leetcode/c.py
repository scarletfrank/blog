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

