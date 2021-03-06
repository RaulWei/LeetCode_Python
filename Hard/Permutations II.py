# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
注意
1 字符串排序 要记得先对nums排序
2 已经排序 选择下一个数字的时候避免和上一次选择重复
'''

import copy

# :type nums: List[int]
# :rtype: List[List[int]]
class Solution(object):
    def permuteUnique(self, nums):
        book = [0 for i in range(len(nums))]
        res_t = [0 for i in range(len(nums))]
        res = []
        nums.sort()
        self.backtracking(0, nums, res_t, res, book)
        return res

    def backtracking(self, step, nums, res_t, res, book):
        if step == len(nums):
            res.append(copy.deepcopy(res_t))
            return
        i = 0
        while i < len(nums):
            if book[i] == 0:
                res_t[step] = nums[i]
                book[i] = 1
                self.backtracking(step + 1, nums, res_t, res, book)
                book[i] = 0
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    # 避免回溯时和上次选择重复
                    i += 1
            i += 1

if __name__ == '__main__':
    sol = Solution()
    sol.permuteUnique([1, 2, 1])