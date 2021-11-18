'''
Date: 2021-11-15 11:11:02
LastEditors: Chenhuiyu
LastEditTime: 2021-11-15 11:13:55
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
    # 辅助函数
    def connectTwo(self, node1, node2):
        if node1 is None or node2 is None:
            return None
        # 将传入的两个节点连接
        node1.next = node2
        # 连接相同父节点的两个子节点
        self.connectTwo(node1.left, node1.right)
        self.connectTwo(node2.left, node2.right)
        # 连接跨越父节点的两个子节点
        self.connectTwo(node1.right, node2.left)

    # 主函数
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        self.connectTwo(root.left, root.right)
        return root


# @lc code=end
