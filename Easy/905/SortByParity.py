from collections import deque

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        dq = deque()
        for num in A:
            if num % 2 == 0:
                dq.appendleft(num)
            else:
                dq.append(num)
        return list(dq)

solution = Solution()
testArr = [3, 1, 2, 4]
print("Expecting [2, 4, 3, 1]\n" +
      "Returned: ")
print solution.sortArrayByParity(testArr)