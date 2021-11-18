'''
Date: 2021-11-15 11:34:05
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 11:38:00
FilePath: \\.leetcode\\114.二叉树展开为链表.py
'''

#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        # 1.将左右子树拉平
        flatten(root.left)
        flatten(root.right)
        # 2.将左子树变成右子树
        #   2.1记录原有的左右子树副本
        left_ori = root.left
        right_ori = root.right
        #   2.2左子树设空，右子树变为左子树
        root.left = None
        root.right = left_ori
        # 3.原有的右子树接到现在的右子树下面
        p = root
        while p.right is not None:
            p = p.right
        p.right = right_ori


# @lc code=end
