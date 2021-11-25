#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2):
        # 合并两个链表，传入参数：两个有序链表的头结点
        # 返回合并后的头结点和尾结点
        dummyHead = ListNode()
        p1 = head1
        p2 = head2
        cur = dummyHead
        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                cur.next = p2
                p2 = p2.next
            else:
                cur.next = p1
                p1 = p1.next
            cur = cur.next
        while p1 is not None:
            cur.next = p1
            p1 = p1.next
            cur = cur.next
        while p2 is not None:
            cur.next = p2
            p2 = p2.next
            cur = cur.next

        return dummyHead.next, cur

    def ththn(self, First, subLength):
        # 传入参数First和subLength，分别是头结点和需要合并的链表的长度
        # 返回左组的头，左组的尾，右组的头，右组的尾，和合并后整组的next
        leftHead = First
        leftTail = First
        rightHead = None
        rightEnd = None
        subNext = None

        # 如果有左组也有右组
        pass_index = 0
        while First is not None:
            pass_index += 1
            # 左组的尾
            if pass_index <= subLength:
                leftTail = First
            # 右组的头
            if pass_index == subLength + 1:
                rightHead = First
            # 右组的尾
            if pass_index > subLength:
                rightEnd = First
            # 超过两杯长度跳出循环
            if pass_index == 2 * subLength:
                break
            # 循环指针跳下一个
            First = First.next
        # 断开左组的尾
        leftTail.next = None
        # 记录并断开右组的尾
        if rightEnd.next is not None:
            subNext = rightEnd.next
            rightEnd.next = None
        return leftHead, leftTail, rightHead, rightEnd, subNext

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 求得整个链表的长度
        cur = head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1

        # subLength表示两个需要合并的链表的长度，合并后的长度为2*subLength
        subLength = 1
        First = head
        while subLength <= length:
            while First is not None:
                leftHead, leftTail, rightHead, rightEnd, subNext = self.ththn(First, subLength)
                First = subNext
                mergeHead, mergeTail = self.merge(leftHead, rightHead)
                mergeTail.next = subNext


# @lc code=end
