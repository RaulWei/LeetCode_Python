# -*- coding: UTF-8 -*-
__author__ = 'weimw'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# :type head: ListNode
# :type x: int
# :rtype: ListNode
class Solution(object):
    def partition(self, head, x):
        # 特殊情况考虑
        if not head:
            return None

        # 比x小的放在low链表 大于等于x的放在high链表
        p = head
        low, high = None, None
        retHead, retMide = None, None
        while p:
            if p.val < x:
                if low is None:
                    low = p
                    retHead = low
                else:
                    low.next = p
                    low = low.next
            else:
                if high is None:
                    high = p
                    retMide = high
                else:
                    high.next = p
                    high = high.next
            p = p.next

        # 返回结果处理
        if low is None:
            high.next = None
            return retMide
        if high is None:
            low.next = None
            return retHead
        high.next = None
        low.next = retMide
        return retHead

if __name__ == '__main__':
    p1 = ListNode(2)
    p2 = ListNode(1)
    p1.next = p2
    sol = Solution()
    sol.partition(p1, 2)
