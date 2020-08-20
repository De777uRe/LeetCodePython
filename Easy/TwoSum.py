from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_target_pair = {}
        for i, num in enumerate(nums):
            target_num = target - num
            if target_num in nums_to_target_pair:
                return [nums.index(target_num), i]
            nums_to_target_pair[num] = target_num
        for num, complement in nums_to_target_pair.items():
            index_of_num = nums.index(num)
            if num == complement:
                if nums.count(num) > 1:
                    return [index_of_num, nums[index_of_num+1:].index(complement) + index_of_num + 1]
                else:
                    continue
            elif complement in nums:
                return [index_of_num, nums.index(complement)]


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print("Expecting [0, 1]: " + str(solution.twoSum(nums, target)))
nums = [3, 2, 4]
target = 6
print("Expecting [1, 2]: " + str(solution.twoSum(nums, target)))
nums = [3, 3]
target = 6
print("Expecting [0, 1]: " + str(solution.twoSum(nums, target)))
nums = [2, 5, 5, 11]
target = 10
print("Expecting [1, 2]: " + str(solution.twoSum(nums, target)))
