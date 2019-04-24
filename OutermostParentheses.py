class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        substr = ""
        index = 0
        while index < len(S)-1:
            if S[index] == S[index+1] and S[index] == '(':
                for j in range(index+1, len(S)-1, 1):
                    if S[j] == ')' and S[j+1] == ')':
                        substr += S[j]
                        index = j
                        break
                    else:
                        substr += S[j]
                result += substr
                substr = ""
            index += 1

        return result


solutionObj = Solution()
# expected = solutionObj.removeOuterParentheses("(()())(())")
expected = solutionObj.removeOuterParentheses("(()())(())(()(()))")
print(expected)
