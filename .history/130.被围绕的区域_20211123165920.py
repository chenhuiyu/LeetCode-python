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
        m = len(board)
        n = len(board[0])
        for i in range(m):
            infection(board, i, 0)
        for i in range(m):
            infection(
                board,
                i,
            )
        for j in range(n):
            print(board[0][j])
            infection(board, 0, j)

        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"

    def infection(board, i, j):
        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
            return
        if board[i][j] == "O":
            board[i][j] = "A"
            infection(board, i + 1, j)
            infection(board, i - 1, j)
            infection(board, i, j + 1)
            infection(board, i, j - 1)


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

# @lc code=end
