'''
Date: 2021-11-16 15:18:58
LastEditors: Chenhuiyu
LastEditTime: 2021-11-16 15:23:00
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
        # 计算当前节点高度
        def height(root):
            if root is None:
                return 0
            # 当前节点的高度等于左右子树中较大的高度加一
            return max(height(root.left), height(root.right)) + 1

        # 判断当前节点是否是平衡的
        def balance(root):
            if root is None:
                return True
            # 平衡条件：左子树平衡、右子树平衡，左右子树高度差不大于1
            if balance(root.left) is True and balance(root.right) is True and abs(height(root.left) - height(root.right)) <= 1:
                return True
            else:
                return False

        return balance(root)


# @lc code=end
