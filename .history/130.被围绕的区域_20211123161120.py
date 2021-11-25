#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#


# @lc code=start
class Solution:
    def __init__(self, bool_ans):
        self.bool_ans = bool_ans

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def infection(board, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                self.bool_ans = False
                return
            if board[i][j] == "O":
                board[i][j] = "."
                infection(board, i + 1, j, self.bool_ans)
                infection(board, i, j + 1, self.bool_ans)
                infection(board, i - 1, j, self.bool_ans)
                infection(board, i, j - 1, self.bool_ans)

        bool_board = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    print(i, j)
                    self.bool_ans = True
                    infection(board, i, j, self.bool_ans)
                    bool_board[i][j] = 1 if self.bool_ans is True else 0


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

# @lc code=end
