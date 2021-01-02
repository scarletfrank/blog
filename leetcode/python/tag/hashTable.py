from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start:start + L] == needle:
                return start
        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force => Time Limit Exceeded
        # One-pass Hash Table
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if str(complement) in d:
                return [d.get(str(complement)), i]
            d[str(nums[i])] = i

    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for num in nums:
            if num not in duplicate:
                duplicate[num] = 1
            else:
                return True
        return False
        # shortcut: return len(nums) != len(set(nums))
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        duplicate = {}
        for i, num in enumerate(nums):
            if num not in duplicate:
                duplicate[num] = i
            else:
                # 一定遇到了重复的数字
                # 只要存在一个符合条件的就能返回True
                if abs(duplicate[num] - i) <= k:
                    return True
                else:
                    duplicate[num] = i # 重新出发
        return False
    
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        duplicate = {}
        # 相比二，数字也有一个差距条件
        for i, num in enumerate(nums):
            pass
        pass
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = {}
        cnt = 0
        m[nums[0]] = 1 # FIRST ELEMENT 
        for i in range(1, len(nums)):
            if nums[i] in m:
                # 向后序列数字一定满足 i < j
                # good pairs数量应该增加前面的数量
                print(nums[i], i, cnt)
                cnt += nums[i]
                nums[i] += 1 
            else:
                m[nums[i]] = 1 # 第一个
        return cnt
    def findKthPositive(self, arr: List[int], k: int) -> int:
        pm = {}
        for a in arr:
            pm[a] = 1  # exists
        cnt = 0
        for i in range(1, len(arr) + k + 1):  # [1...n] positive seq
            if i not in pm:
                cnt += 1
            if cnt == k:
                return i 
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for a in arr:
            if a in m:
                m[a] += 1 
            else:
                m[a] = 1
                
if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,1,1,3]
    arr = [1,2,2,1,1,3]
    print(sol.numIdenticalPairs(nums))
