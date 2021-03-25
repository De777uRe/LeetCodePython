class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        streak = ""
        paren_stack = []
        for i in range(len(S)):
            if i == 0:
                paren_stack.append(S[i])
            else:
                if S[i] == '(':
                    if len(paren_stack) >= 1:
                        streak += S[i]
                    paren_stack.append(S[i])
                else:
                    if len(paren_stack) == 1:
                        paren_stack = []
                        result += streak
                        streak = ""
                    else:
                        streak += S[i]
                        paren_stack.pop()
        return result


solutionObj = Solution()
expected = solutionObj.removeOuterParentheses("(()())(())")
# expected = solutionObj.removeOuterParentheses("(()())(())(()(()))")
print(expected)
