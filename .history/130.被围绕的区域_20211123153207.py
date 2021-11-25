#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def infection(borad, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O":
                return
            if board[i][j] == "O":
                board[i][j] = "."
                infection(board, i + 1, j)
                infection(board, i, j + 1)
                infection(board, i - 1, j)
                infection(board, i, j - 1)
                board[i][j] = "O"

        for i in range(len(board)):
            for j in range(len(board[0])):
                infection(board, i, j)


# @lc code=end
