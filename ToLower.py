class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


solution = Solution()
testString1 = "LOWER"
testString2 = "Upper"
testString3 = "TeStStRiNG"

testValues = [testString1, testString2, testString3]

print("Expecting lower, upper, teststring\n" +
      "Returned: ")
for string in testValues:
    print(solution.toLowerCase(string))
