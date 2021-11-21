#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None
        cur = head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1


# @lc code=end
