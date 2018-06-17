class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0

        for jewel in J:
            for stone in S:
                if jewel == stone:
                    count += 1

        return count


solution = Solution()
jewel_1 = "aA"
stone_1 = "aAAbbbb"
print(str(solution.numJewelsInStones(jewel_1, stone_1)))
