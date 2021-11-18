'''
Date: 2021-11-14 17:25:22
LastEditors: Chenhuiyu
LastEditTime: 2021-11-14 17:29:31
FilePath: \\.leetcode\\142.环形链表-ii.py
'''
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return None
        slow = head.next
        fast = head.next.next
        while fast is not None:
            if slow != fast:
                slow = slow.next
                fast = fast.next.next
            else:
                break


# @lc code=end
