class Solution:
    def reverse(self, x: int) -> int:
        if 10 > x >= 0:
            return str(x)

        ret_str = ""

        if x < 0:
            ret_str = "-"
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

    def new_reverse(self, x: int) -> int:
        num_string = str(x)
        reversed_string = []
        is_negative = False
        for i in range(len(num_string)-1, -1, -1):
            if num_string[i] == '-':
                is_negative = True
                continue
            reversed_string.append(num_string[i])
        final_num = int("".join(reversed_string))
        if is_negative:
            final_num *= -1
        if final_num > 2 ** 31 - 1 or final_num < -2 ** 31:
            return 0
        else:
            return final_num


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(1534236469))
    print(solution.new_reverse(123))
    print(solution.new_reverse(-123))
    print(solution.new_reverse(120))
    print(solution.new_reverse(1534236469))


