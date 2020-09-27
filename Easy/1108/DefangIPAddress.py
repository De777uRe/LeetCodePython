class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


solution = Solution()
ip_1 = "1.1.1.1"
result = solution.defangIPaddr(ip_1)
print(result)

