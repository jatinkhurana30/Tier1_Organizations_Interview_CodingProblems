"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid) -> int:
        i = 0
        j = 0
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    count += 1
                    grid = self.findIsland(grid, i, j, m, n)
        return count

    def findIsland(self, grid, i, j, m, n):
        if i > m - 1 or j > n - 1:
            return grid

        if grid[i][j] == '1':
            grid[i][j] = '0'

        if j+1 < n and grid[i][j + 1] == '1':
            self.findIsland(grid, i, j + 1, m, n)

        if i+1 < m and grid[i + 1][j] == '1':
            self.findIsland(grid, i + 1, j, m, n)

        if i -1 >= 0 and grid[i - 1][j] == '1':
            self.findIsland(grid, i - 1, j, m, n)

        if j - 1 >= 0 and grid[i][j-1] == '1':
            self.findIsland(grid, i, j-1, m, n)

        return grid


# grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
print(Solution().numIslands(grid))
