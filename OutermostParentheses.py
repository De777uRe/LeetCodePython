class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        indices = []
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                if S[i] == '(':
                    indices.append(i)
                else:
                    indices.append(i+1)

        for j in range(len(indices)-1):
            result += S[indices[j]+1:indices[j+1]]

        return result


solutionObj = Solution()
expected = solutionObj.removeOuterParentheses("(()())(())(()(()))")
print(expected)
