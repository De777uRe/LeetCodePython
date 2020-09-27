from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = []
        for num in nums:
            sum += num
            result.append(sum)
        return result


def test_1():
    solution = Solution()
    assert solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]


if __name__ == "__main__":
    test_1()
