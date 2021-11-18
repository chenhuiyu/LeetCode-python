'''
Date: 2021-10-18 11:57:40
LastEditors: Chenhuiyu
LastEditTime: 2021-10-18 14:54:04
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
        pre_node = ListNode(None)
        cur_node = ListNode(None)
        head_node = pre_node
        while l1 is not None or l2 is not None:
            if l1 is None:
                n1 = 0
            elif l2 is None:
                n2 = 0
            else:
                n1 = l1.val
                n2 = l2.val
                l1 = l1.next
                l2 = l2.next
            val = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            cur_node = ListNode(val)
            pre_node.next = cur_node
            pre_node = cur_node
        if carry == 1:
            cur_node = ListNode(1)
            pre_node.next = cur_node
        return head_node.next


# @lc code=end
