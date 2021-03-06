# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
双指针 一快一慢
具体推倒 https://leetcode.com/discuss/9908/o-n-solution-by-using-two-pointers-without-change-anything
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return 如果存在环 返回快慢指针相交的位置 不存在返回None
    def beginCycle(self, head):
        p1, p2 = head, head
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if not p2:
                return None
            p2 = p2.next
            if p1 == p2:
                return p1

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        p1, p2 = head, self.beginCycle(head)
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None

if __name__ == '__main__':
    sol = Solution()
    p1 = ListNode(1)
    p2 = ListNode(2)
    p1.next = p2
    p2.next = p1
    sol.detectCycle(p1)