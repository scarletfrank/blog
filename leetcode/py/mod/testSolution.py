from solution import Solution
# VS Code resolve .solution but debug will failed 

import unittest

class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        sol = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(sol.twoSum(nums, target), [0, 1])

    def test_countPrimes(self):
        sol = Solution()
        n = 10
        self.assertEqual(sol.countPrimes(n), 4)
    def testIsomorphic(self):
        """
        docstring
        """
        sol = Solution()
        s, t = "foo", "bar"
        self.assertEqual(sol.isIsomorphic(s, t), False)
        
if __name__ == '__main__':
    unittest.main()