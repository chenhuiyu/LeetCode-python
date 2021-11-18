'''
Date: 2021-11-15 11:09:01
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 11:10:30
FilePath: \\.leetcode\\226.翻转二叉树.py
'''

#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# @lc code=end
