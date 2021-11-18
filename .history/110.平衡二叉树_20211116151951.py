'''
Date: 2021-11-16 15:18:58
LastEditors: Chenhuiyu
LastEditTime: 2021-11-16 15:19:51
FilePath: \\.leetcode\\110.平衡二叉树.py
'''

#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right))


# @lc code=end
