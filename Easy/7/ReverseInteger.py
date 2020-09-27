class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return "0"

        ret_str = "" if x >= 0 else "-"

        if x < 0:
            x *= -1

        while x > 0:
            if ret_str == "" or ret_str == "-":
                if x % 10 == 0:
                    x //= 10
                    continue
            ret_str += str(x % 10)
            x //= 10

        if int(ret_str) > 2147483647 or int(ret_str) < -2147483648:
            return "0"

        return ret_str


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(1534236469))


