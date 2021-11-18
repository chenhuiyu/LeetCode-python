'''
Date: 2021-10-18 11:57:40
LastEditors: Chenhuiyu
LastEditTime: 2021-10-18 14:46:22
FilePath: \\leetcode_pythonc:\\Users\\Administrator\\.leetcode\\2.两数相加.py
'''

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        pre_node = None
        cur_node = None
        while l1 is not None and l2 is not None:
            if l1 is None:
                n1 = 0
            elif l2 is None:
                n2 = 0
            else:
                n1 = l1.val
                n2 = l2.val
            pre_node = cur_node
            val = (n1 + n2 + carry) % 10
            carry = (n1 + n2) // 10
            cur_node = ListNode(val)
            cur_node.next = pre_node
        if carry == 1:
            pre_node = cur_node
            cur_node = ListNode(1)
            cur_node.next = pr


# @lc code=end
