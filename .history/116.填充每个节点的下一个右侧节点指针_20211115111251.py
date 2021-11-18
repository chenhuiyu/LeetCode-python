'''
Date: 2021-11-15 11:11:02
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 11:12:39
FilePath: \\.leetcode\\116.填充每个节点的下一个右侧节点指针.py
'''
#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connectTwo(self, node1, node2):
        node1.next = node2
        self.connectTwo(node1.left, node1.right)
        self.connectTwo(node2.left, node2.right)
        self.connectTwo(node1.right, node2.left)

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        self.connectTwo(root.left, root.right)


# @lc code=end
