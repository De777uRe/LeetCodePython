from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        ordered_list = []
        reversed_list = []

        while x > 9:
            right_most = x % 10
            ordered_list.append(right_most)
            reversed_list.append(right_most)
            x //= 10

        ordered_list.append(x)
        reversed_list.append(x)

        while len(reversed_list) > 0:
            if reversed_list.pop() != ordered_list.pop(0):
                return False

        return True

    def onlineSolution(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        return x == revertedNumber or x == revertedNumber//10


solution = Solution()
num = 121
print("Expecting True: " + str(solution.isPalindrome(num)))
print("Expecting True: " + str(solution.onlineSolution(num)))
