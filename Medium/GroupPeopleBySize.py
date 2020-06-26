from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = {}
        for i in range(len(groupSizes)):
            if result.get(groupSizes[i]) is None:
                result[groupSizes[i]] = [i]
            elif len(result[groupSizes[i]]) < groupSizes[i]:
                result[groupSizes[i]].append(i)
            else:
                smallest_list = min(result[groupSizes[i]], key=len)
                smallest_list.append(i)
        output = []
        for groupList in result.values():
            if any(isinstance(el, list) for el in groupList):
                for subList in groupList:
                    output.append(subList)
            else:
                output.append(groupList)
        output.sort(key=len)
        return output



def test_1():
    solution = Solution()
    assert solution.groupThePeople([2, 1, 3, 3, 3, 2]) == [[1], [0, 5], [2, 3, 4]]


if __name__ == "__main__":
    test_1()
