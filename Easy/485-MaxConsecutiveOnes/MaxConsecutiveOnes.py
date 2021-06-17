from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longestConsecutive = 0
        currentStreak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currentStreak += 1
                longestConsecutive = max(longestConsecutive, currentStreak)
            else:
                currentStreak = 0
        return longestConsecutive


if __name__ == "__main__":
    solution = Solution()
    testcase1 = [1, 1, 0, 1, 1, 1] # Expect 3
    print(solution.findMaxConsecutiveOnes(testcase1))