from typing import List

'''
Approaches:
    1. Naive: Sort arrays first, then iterate keeping track of longest sequence
        Complexity would be O(n*log(n)) + O(n) = O(n)
    2. Start from max, find numbers max-1
            If no max-1 found, remove max, find next max, continue
            If found max-1, find max-2, etc.
        This approach is not acceptable at O(n^2)
    3. Best: Iterate through initial list, adding all seen to list
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)
        return longest_streak

    def longestConsecutiveBest1(self, nums: List[int]) -> int:
        seen = set()
        longest_sequence = 1
        for num in nums:
            sequence = 1
            if num not in seen:
                seen.add(num)
                i = num + 1
                while i in nums:
                    seen.add(i)
                    sequence += 1
                    i += 1
                i = num - 1
                while i in nums:
                    seen.add(i)
                    sequence += 1
                    i -= 1
            longest_sequence = max(sequence, longest_sequence)
        return longest_sequence

    def longestConsecutive1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_unique_nums = sorted(list(set(nums)))
        sequence = 1
        longest_sequence = 1
        i = 0
        while i < len(sorted_unique_nums)-1:
            if sorted_unique_nums[i+1] - sorted_unique_nums[i] == 1:
                sequence += 1
                i += 1
            else:
                longest_sequence = max(sequence, longest_sequence)
                if sequence == 1:
                    i += 1
                else:
                    sequence = 1
        longest_sequence = max(sequence, longest_sequence)
        return longest_sequence


    def longestConsecutiveBad(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_num = max(unique_nums)
        nums.remove(max_num)
        sequence = 1
        longest_sequence = 1
        while len(unique_nums) > 0:
            sequence_found = False
            for num in unique_nums:
                if num == max_num - 1:
                    max_num = num
                    sequence += 1
                    unique_nums.remove(max_num)
                    sequence_found = True
                    break
            if not sequence_found:
                max_num = max(unique_nums)
                unique_nums.remove(max_num)
            longest_sequence = max(sequence, longest_sequence)
        return longest_sequence


if __name__ == "__main__":
    solution = Solution()
    testcase1 = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(testcase1))
    testcase2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(solution.longestConsecutive(testcase2))
