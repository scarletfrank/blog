from typing import List

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