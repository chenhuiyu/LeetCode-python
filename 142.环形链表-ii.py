'''
Date: 2021-11-14 17:25:22
LastEditors: Chenhuiyu
LastEditTime: 2021-11-14 17:38:07
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
        while fast != slow:
            if fast.next is None or fast.next.next is None:
                return None
            else:
                slow = slow.next
                fast = fast.next.next
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


# @lc code=end
