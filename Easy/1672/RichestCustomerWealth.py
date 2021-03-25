from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthiest_customer = None
        max_amount = -1
        for i, customer in enumerate(accounts):
            total = sum(customer)
            if total > max_amount:
                max_amount = total
                wealthiest_customer = i


def test_1():
    solution = Solution()
    assert solution.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6


if __name__ == "__main__":
    test_1()
