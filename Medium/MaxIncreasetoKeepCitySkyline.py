from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sum = 0
        vertical_maxes = []
        for building in grid:
            vertical_maxes.append(max(building))

        horizontal_maxes = []
        transpose = []
        for i in range(len(grid[0])):
            for building in grid:
                transpose.append(building[i])
            horizontal_maxes.append(max(transpose))
            transpose.clear()

        for j in range(len(grid)):
            for k in range(len(grid[0])):
                bldg_height = min(vertical_maxes[j], horizontal_maxes[k])
                if grid[j][k] < bldg_height:
                    sum += (bldg_height - grid[j][k])

        return sum



solver = Solution()
test = [ [3, 0, 8, 4],
         [2, 4, 5, 7],
         [9, 2, 6, 3],
         [0, 3, 1, 0] ]
print(solver.maxIncreaseKeepingSkyline(test))
