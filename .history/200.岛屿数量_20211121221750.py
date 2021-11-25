#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]


# @lc code=start
class Solution:
    def infection(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "2"
        self.infection(grid, i + 1, j)
        self.infection(grid, i - 1, j)
        self.infection(grid, i, j + 1)
        self.infection(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.infection(grid, i, j)
        return res


# @lc code=end
