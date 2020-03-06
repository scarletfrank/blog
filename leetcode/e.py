from typing import List
class Solution:
    # smallest missing positive integer
    # Theta (n) constant extra space
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < n and nums[nums[i] - 1] != nums[i]:
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    ans = ans + (left_max - height[l])
                l = l + 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    ans = ans + (right_max - height[r])
                r = r - 1
        return ans
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        pos = [0] * (m+n)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                Sum = mul + pos[i+j+1]
                pos[i+j] = pos[i+j] + (Sum//10)
                pos[i+j+1] = Sum % 10
        res = []
        for p in pos:
            if p != 0 or len(res) != 0:
                res.append(str(p))
        if len(res) == 0:
            return "0"
        else:
            return "".join(res)
