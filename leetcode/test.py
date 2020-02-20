from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
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
            head = head.next
        cnt += 1
        cur = cur.next
    return head

def printLL(head: ListNode):
    temp = head
    while temp is not None:
        print(temp.val)
        temp = temp.next

def intToRoman(num:int) -> str:
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

def romanToInt(s: str) -> int:
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

nums = 3
s = "MCMXCIV"
print(romanToInt(s))
