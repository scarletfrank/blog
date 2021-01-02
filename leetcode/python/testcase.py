from tag.hashTable import Solution

import unittest

class TestSolution(unittest.TestCase):
    def test_strStr(self):
        sol = Solution()
        haystack = "hello"
        needle = "ll"
        target = 2
        self.assertEqual(sol.strStr(haystack, needle), target)
    
    def test_findKthPositive(self):
        sol = Solution()
        arr = [2, 3, 4, 7, 11]
        k = 5
        target = 9
        self.assertEqual(sol.findKthPositive(arr, k), target)

if __name__ == '__main__':
    unittest.main()