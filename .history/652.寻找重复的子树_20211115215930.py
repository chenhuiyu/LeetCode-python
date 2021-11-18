'''
Date: 2021-11-15 21:57:07
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 21:59:27
FilePath: \\.leetcode\\652.寻找重复的子树.py
'''

#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # 将所有子树序列化
        def help(root):
            if root is None:
                return "#"
            # 序列化左子树
            left = help(root.left)
            # 序列化右子树
            right = help(root.right)
            serial_subtree = left + "," + str(root.val) + "," + right


# @lc code=end
