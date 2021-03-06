# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
实际上就是实现二叉搜索树的中序遍历 迭代写法
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.root = root
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        # 是否有下一个最小值
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        # 求下一个最小值
        res = self.stack.pop()
        self.pushAll(res.right)
        return res.val

    def pushAll(self, root):
        while root:
            self.stack.append(root)
            root = root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())