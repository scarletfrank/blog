class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        USA => True
        Flag => True
        FlaG => True
        Non-empty word
        """
        cnt, flag  = 0, 0 
        for c in word:
            if c.isupper(): # ord() judge
                cnt = cnt + 1

        if cnt == 0 or cnt == len(word):
            flag = 1 # Correct
        elif cnt == 1 and word[0].isupper():
            flag = 1
        else:
            flag = 0 # Wrong
        return bool(flag)

word = "Leetcode"
sol = Solution()
print(sol.detectCapitalUse(word))
        