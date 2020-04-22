class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found_chars = []
        substrings = []
        substring = ''
        i = 0
        while i < len(s):
            if s[i] not in found_chars:
                found_chars.append(s[i])
                substring += s[i]
                i += 1
            else:
                substrings.append(substring)
                substring = ''
                found_chars.clear()
                s = s[1:]
                i = 0
        substrings.append(substring)
        return len(max(substrings, key=len))


solution = Solution()
test1 = "abcabcbb"
print("Expecting 3: {}".format(solution.lengthOfLongestSubstring(test1)))
test2 = "bbbbb"
print("Expecting 1: {}".format(solution.lengthOfLongestSubstring(test2)))
test3 = "pwwkew"
print("Expecting 3: {}".format(solution.lengthOfLongestSubstring(test3)))
test4 = "dvdf"
print("Expecting 3: {}".format(solution.lengthOfLongestSubstring(test4)))
test5 = "anviaj"
print("Expecting 5: {}".format(solution.lengthOfLongestSubstring(test5)))
