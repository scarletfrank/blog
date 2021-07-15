from logging import basicConfig
from typing import List
from collections import Counter
from itertools import chain
import math

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
                    duplicate[num] = i  # 重新出发
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
        m[nums[0]] = 1  # FIRST ELEMENT
        for i in range(1, len(nums)):
            if nums[i] in m:
                # 向后序列数字一定满足 i < j
                # good pairs数量应该增加前面的数量
                print(nums[i], i, cnt)
                cnt += nums[i]
                nums[i] += 1
            else:
                m[nums[i]] = 1  # 第一个
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

    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {'l': 2, 'o': 2, 'b': 1, 'a': 1, 'n': 1}
        cnter = Counter(text)
        num = []
        for k in balloon:
            judge = cnter[k] // balloon[k]  # 整除
            num.append(judge)
        return min(num)

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(c) == len(set(c.values()))

    # 糖果节制，用集合统计糖果类型比哈希表更快（那你这题为啥分类成哈希表）
    def distributeCandies(self, candyType: List[int]) -> int:
        candyCounter = set(candyType)  # Counter => set
        return min(len(candyType)//2, len(candyCounter))

    # 找出 t 比 s 多的一个字母
    # 看到最本质的方法是直接计算相差的ascii数字
    def findTheDifference(self, s: str, t: str) -> str:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        for i in cnt_t:
            if cnt_t[i] - cnt_s[i] == 1:
                return i

    # 这不是集合的题目吗 哪里是哈希表了
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    # 集合比哈希还快 ?
    # 似乎差不多
    def repeatedNTimes(self, A: List[int]) -> int:
        """
        k = set()
        for i in A:
            if i in k:
                return i
            else:
                k.add(i)
        """
        n = len(A) // 2
        cnt = Counter(A)
        for i in cnt:
            if cnt[i] > 1:
                return i 

    def countCharacters(self, words: List[str], chars: str) -> int:
        sum, chars_counter = 0, Counter(chars)
        for word in words:
            word_counter = Counter(word)
            for c in word_counter:
                if word_counter[c] > chars_counter[c]:
                    break
            else:
                sum += len(word)
        return sum
    """

    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        s = set(nums1 + nums2)
        result = []
        for i in s:
            if i in cnt1 and i in cnt2:
                result += [i] * min(cnt1[i], cnt2[i])
        return result

    def findRestaurant_naive(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        naive solution of https://leetcode.com/problems/minimum-index-sum-of-two-lists/
        """
        cnt1 = {v:i for i, v in enumerate(list1)}
        cnt2 = {v:i for i, v in enumerate(list2)}
        common = set(list1).intersection(set(list2))
        com_m = {}
        for c in common:
            com_m[c] = cnt1[c] + cnt2[c]
        min_value = min(com_m.items(), key=lambda x: x[1])[1]
        output = [x[0] for x in com_m.items() if x[1] == min_value]
        return output
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        linear solution of https://leetcode.com/problems/minimum-index-sum-of-two-lists/
        """
        cnt1 = {v:i for i, v in enumerate(list1)}
        min_sum, res = math.inf, []
        for i, e in enumerate(list2):
            if e in cnt1:
                sum = i + cnt1[e]
                if sum < min_sum:
                    res.clear()
                    res.append(e)
                    min_sum = sum
                elif sum == min_sum:
                    res.append(e)
        return res
    
    def canFormArray_naive(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # basic case
        if Counter(arr) != Counter(chain.from_iterable(pieces)):
            return False
        # piece which len() > 1
        arm = {}
        for i, a in enumerate(arr):
            arm[a] = i
        for key in list(filter(lambda p: len(p) > 1, pieces)):
            e, l = key[0], len(key)
            k = arm[e]
            if key != arr[k: k + l]:
                return False
        return True
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece = {p[0]:p for p in pieces}
        res = []
        for num in arr:
            res += piece.get(num, [])
            
        return res == arr

if __name__ == '__main__':
    sol = Solution()
    arr = [91,4,64,78]
    pieces = [[78],[4,64],[91]]
    result = sol.canFormArray(arr, pieces)
    print(result)
