from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        islands = []
        seen = set()
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    if (i, j) not in seen:
                        neighbors = [(i, j)]
                        island = self.getFloodFillNeighbors(i, j, grid, len(grid), len(grid[0]), neighbors, seen)
                        islands.append(island)

        closed_island_count = 0
        for island in islands:
            if self.isIslandClosed(island, len(grid), len(grid[0])):
                closed_island_count += 1
        return closed_island_count

    def getFloodFillNeighbors(self, i, j, grid, num_rows, num_cols, neighbors, seen):
        initial_neighbor = (i, j)
        seen.add(initial_neighbor)
        steps = [
            (0, 1),  # right
            (0, -1),  # left
            (1, 0),  # down
            (-1, 0),  # up
        ]
        for step in steps:
            neighbor = (i + step[0], j + step[1])
            if self.isInGrid(neighbor[0], neighbor[1], num_rows, num_cols):
                if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in seen:
                    neighbors.append(neighbor)
                    self.getFloodFillNeighbors(neighbor[0], neighbor[1], grid, num_rows, num_cols, neighbors, seen)
        return neighbors

    def isInGrid(self, i, j, num_rows, num_cols):
        if i < num_rows and j < num_cols and i >= 0 and j >= 0:
            return True
        return False

    def isIslandClosed(self, island, num_rows, num_cols):
        for coordinate in island:
            if coordinate[0] == 0 or coordinate[0] == num_rows - 1 or coordinate[1] == 0 or coordinate[ 1] == num_cols - 1:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]
    print(solution.closedIsland(grid))
