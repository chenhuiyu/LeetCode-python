#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 计算限制数组
        row = [[0 for i in range(9)] for j in range(9)]
        col = [[0 for i in range(9)] for j in range(9)]
        bucket = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                k = 3 * (i // 3) + j // 3
                num = int(board[i][j])


# @lc code=end
