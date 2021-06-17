from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        found_chars = []
        substrings = []
        substring = ''
        i = 0
        max_len = 0
        while i < len(s):
            if s[i] not in found_chars:
                found_chars.append(s[i])
                substring += s[i]
                i += 1
                if i > max_len:
                    max_len = i
            else:
                substrings.append(substring)
                substring = ''
                found_chars.clear()
                s = s[1:]
                i = 0
        substrings.append(substring)
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_length = left = 0
        store = defaultdict(int)
        for right, ch in enumerate(s):
            store[ch] += 1
            while store[ch] > 1:
                store[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length


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
