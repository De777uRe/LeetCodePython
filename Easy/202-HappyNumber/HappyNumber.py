class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        new_n = n
        while True:
            total = 0
            while new_n != 0:
                last_digit = new_n % 10
                total += last_digit * last_digit
                new_n //= 10
            if total == 1:
                return True
            if total in seen:
                return False
            new_n = total
            seen.add(new_n)


if __name__ == "__main__":
    solution = Solution()
    test_case1 = 19
    print(solution.isHappy(test_case1))
    test_case2 = 2
    print(solution.isHappy(test_case2))
