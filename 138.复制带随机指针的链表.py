'''
Date: 2021-11-13 21:09:24
LastEditors: Chenhuiyu
LastEditTime: 2021-11-13 22:51:40
FilePath: \\.leetcode\\138.复制带随机指针的链表.py
'''
#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        while cur.next is not None:
            cur_copy = Node(cur.val, cur.next, None)
            cur.next = cur_copy
            cur = cur_copy.next
        cur = head
        while cur.next.next is not None:
            cur_copy = cur.next
            cur_copy.random = cur.random.next if cur.random is not None else None
            cur = cur.next.next
        ori_list = head
        while ori_list.next.next is not None:
            ori_list.next = ori_list.next.next
            ori_list = ori_list.next.next
        copy_head = head
        copy_list = head.next
        while copy_list.next is not None:
            copy_list.next = copy_list.next.next
            copy_list = copy_list.next.next
        return copy_head


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        cur = head
        while cur is not None:
            cur_copy = Node(cur.val, cur.next, None)
            cur.next = cur_copy
            cur = cur_copy.next
        cur = head
        while cur is not None:
            cur_copy = cur.next
            cur_copy.random = cur.random.next if cur.random is not None else None
            cur = cur.next.next if cur.next.next is not None else None

        ori_list = head
        copy_head = head.next

        while ori_list.next.next is not None:
            next_node = ori_list.next
            ori_list.next = ori_list.next.next
            ori_list = next_node

        return copy_head


# @lc code=end
