#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def loopInfo(root):
            # 以root为头结点的数的递归，返回两个值
            # longestPath:以root为头结点的当前最长同值路径的长度
            # sameRootVal:和root.val同值的路径的长度
            if root is None:
                return 0, 0

            leftLongestPath, leftSameRootVal = loopInfo(root.left)


# @lc code=end
