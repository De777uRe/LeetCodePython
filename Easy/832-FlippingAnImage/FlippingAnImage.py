class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            end = len(A[i]) - 1
            j = 0
            while j < end:
                temp = A[i][end]
                A[i][end] = A[i][j]
                A[i][j] = temp
                j = j+1
                end = end-1
            for k in range(len(A[i])):
                A[i][k] = A[i][k] ^ 1
        return A


solution = Solution()
testImage = [
                [1, 1, 0], [1, 0, 1], [0, 0, 0]
            ]
print("Expecting\n[1, 0, 0]\n[0, 1, 0]\n[1, 1, 1]\n" +
      "Returned: ")
for result in solution.flipAndInvertImage(testImage):
    print(result)
