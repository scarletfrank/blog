from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    s = input()
    i = 0
    while i < len(s):
        if s[i] == ']': # backward to search first matching "["
            j, k = i, 0
            while s[j] != '[':
                if s[j] == '|':
                    k = j 
                j = j - 1
            subs = s[j:i+1]
            num = int(s[j+1:k])
            reps = s[k+1:i]
            reps = reps * num
            s = s.replace(subs, reps, 1)
            i = j
        i = i + 1
    print(s)