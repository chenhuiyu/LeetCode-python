#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]


# @lc code=start
class Solution:
    def infection(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 0:
            return

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.infection(grid, i, j)


# @lc code=end
