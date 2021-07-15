from typing import List
import collections
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_map = {}
        for i, point in enumerate(points):
            a, b = point
            dist_map[(a,b)] = a ** 2 + b ** 2
        els =  heapq.nsmallest(k, dist_map.items(), key=lambda item: item[1])
        output = [list(t[0]) for t in els]
        return output
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = {v:i for i, v in enumerate(arr2)}
        arr_front = list(filter(lambda x : x in cnt, arr1))
        arr_end = list(filter(lambda x: x not in cnt, arr1))
        return sorted(arr_front, key=lambda x: cnt[x]) + sorted(arr_end)


if __name__ == "__main__":
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    sol = Solution()
    res = sol.relativeSortArray(arr1, arr2)
    print(res)
