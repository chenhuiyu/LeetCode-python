#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 从board的i,j位置开始，是否能走出word
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                process(board, word, i, j, 0)
        
        def process(board,word,j,k,k):


# @lc code=end
