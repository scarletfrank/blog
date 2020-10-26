import unittest
from src import solution

class TestSolution(unittest.TestCase):

    def test_twoSum(self):
        sol = solution.Solution()
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(sol.twoSum(nums, target), [0, 1])

if __name__ == '__main__':
    unittest.main()