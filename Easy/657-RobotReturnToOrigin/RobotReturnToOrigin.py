class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')


if __name__ == "__main__":
    solution = Solution()
    testcase1 = "UD" # Expect True
    print(solution.judgeCircle(testcase1))