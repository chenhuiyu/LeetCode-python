#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#


# @lc code=start
class Solution:
    def infection(self, board, i, j):
        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
            return
        if board[i][j] == "O":
            board[i][j] = "A"
            self.infection(board, i + 1, j)
            self.infection(board, i - 1, j)
            self.infection(board, i, j + 1)
            self.infection(board, i, j - 1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 遍历边界位置上的O，递归把所有和边界上的O相连的O都修改为"A"
        m = len(board)
        n = len(board[0])

        for i in range(m):
            self.infection(board, i, 0)
        for i in range(m):
            self.infection(board, i, n - 1)
        for j in range(n):
            self.infection(board, 0, j)
        for j in range(n):
            self.infection(board, m - 1, j)

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"


# @lc code=end
