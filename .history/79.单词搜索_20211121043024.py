#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#


# @lc code=start
class Solution:
    def process(board, word, i, j, k):
        # 从board的i,j位置是否能走出word[k:]的部分

        # base case
        # k来到word终止位置，完整走出来了word，返回true
        if k == len(word):
            return True

        # 如果board[i][j]和word[k]上的字符不同，肯定走不出来word，剪枝返回false
        if board[i][j] != word[k]:
            return False

        # 如果i,j来到了边界位置，剪枝返回false
        if i < 0 or i > len(board) or j < 0 or j > len(board[0]):
            return False

        # 判断i,j在四个方向上走是否能走出word[k+1:]，有一个是true就返回true
        # 为了避免走回头路，把已经走过的地方改成0，递归后恢复现场
        temp = board[i][j]
        board[i][j] = 0
        flag = process(board, word, i + 1, j, k + 1) or process(board, word, i - 1, j, k + 1) or process(board, word, i, j + 1, k + 1) or process(board, word, i, j - 1, k + 1)
        board[i][j] = temp

        return flag

    def exist(self, board: List[List[str]], word: str) -> bool:
        # 从board的i,j位置开始，是否能走出word
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if process(board, word, i, j, 0) is True:
                    return True
        return False


# @lc code=end
