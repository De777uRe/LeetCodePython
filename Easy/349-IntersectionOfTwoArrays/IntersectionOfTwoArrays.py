from typing import List

class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        if len(set_nums1) > len(set_nums2):
            return self.set_intersection(set_nums1, set_nums2)
        else:
            return self.set_intersection(set_nums2, set_nums1)

if __name__ == "__main__":
    solution = Solution()
    testset1_1 = [1, 2, 2, 1]
    testset1_2 = [2, 2]
    print(solution.intersection(testset1_1, testset1_2))
