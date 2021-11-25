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
        # 遍历边界位置上的O，递归把所有和边界上的O相连的O都修改为"A"
        for i in range(len(board)):
            board[i][0]

    def infection(board, i, j):
        if i < 0 or i > len(board) or j < 0 or j > len(board[0]) or board[i][j] != "O":
            return
        if board[i][j] == "O":
            board[i][j] = "A"
            infection(board, i, j)
            infection(board, i, j)
            infection(board, i, j)
            infection(board, i, j)


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

# @lc code=end
