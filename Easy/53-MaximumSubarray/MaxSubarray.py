from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        greatest_sum = sum
        i = 1
        while i < len(nums):
            if nums[i] > sum:
                if sum + nums[i] > nums[i]:
                    sum += nums[i]
                else:
                    sum = nums[i]
            else:
                sum += nums[i]
            if sum > greatest_sum:
                greatest_sum = sum
            i += 1
        return greatest_sum


solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(solution.maxSubArray([1]))
print(solution.maxSubArray([5, 4, -1, 7, 8]))
print(solution.maxSubArray([1, 2]))