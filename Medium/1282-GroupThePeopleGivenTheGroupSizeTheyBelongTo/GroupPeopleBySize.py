from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = {}
        for i in range(len(groupSizes)):
            is_list_of_lists = False
            current_id = groupSizes[i]
            if group_map.get(current_id) is None:
                group_map[current_id] = [i]
                continue
            else:
                if any(isinstance(el, list) for el in group_map[current_id]):
                    is_list_of_lists = True

            if is_list_of_lists:
                if all(len(group) == current_id for group in group_map[current_id]):
                    group_map[current_id].append([i])
                else:
                    smallest_list = min(group_map[current_id], key=len)
                    smallest_list.append(i)
            else:
                if len(group_map[current_id]) == current_id:
                    group_to_list_of_lists = [group_map[current_id], [i]]
                    group_map[current_id] = group_to_list_of_lists
                else:
                    group_map[current_id].append(i)

        output = []
        for groupList in group_map.values():
            if any(isinstance(el, list) for el in groupList):
                for subList in groupList:
                    output.append(subList)
            else:
                output.append(groupList)
        # output.sort(key=len)
        return output


def test_1():
    solution = Solution()
    assert solution.groupThePeople([2, 1, 3, 3, 3, 2]) == [[1], [0, 5], [2, 3, 4]]

def test_2():
    solution = Solution()
    assert solution.groupThePeople([3, 3, 3, 3, 3, 1, 3]) == [[5], [0, 1, 2], [3, 4, 6]]

def test_3():
    solution = Solution()
    print(solution.groupThePeople([2, 2, 1, 1, 1, 1, 1, 1]))
    assert solution.groupThePeople([2, 2, 1, 1, 1, 1, 1, 1]) == [[2], [3], [4], [5], [6], [7], [0, 1]]

if __name__ == "__main__":
    test_3()
