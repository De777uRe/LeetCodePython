class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # {} places a variable into a string
        # 0 takes the variable at argument position 0
        # : adds formatting options for this variable (otherwise it would represent decimal)
        # 032 formats the number to 32 digits zero-padded on the left
        # b converts the number to its binary representation
        return '{0:032b}'.format(x ^ y).count('1')


solution = Solution()
print(solution.hammingDistance(1, 4))
