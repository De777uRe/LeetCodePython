class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}

        res = 0
        for i, letter in enumerate(s):
            if i < len(s) - 1:
                if symbol_map[letter] < symbol_map[s[i+1]]:
                    res -= symbol_map[letter]
                    continue
            res += symbol_map[letter]

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("IV"))
    print(solution.romanToInt("IX"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))

solution = Solution()

def test_RN_3():
    assert solution.romanToInt("III") == 3

def test_RN_4():
    assert solution.romanToInt("IV") == 4

def test_RN_9():
    assert solution.romanToInt("IX") == 9

def test_RN_58():
    assert solution.romanToInt("LVIII") == 58

def test_RN_1994():
    assert solution.romanToInt("MCMXCIV") == 1994
