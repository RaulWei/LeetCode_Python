# -*- coding: UTF-8 -*-
__author__ = 'wang'

import math

'''
给定无序数组 找出排序后的序列中两个相邻元素之间的最大差值
这种偏数学题的 需要注意很多边界的题目做起来还是很操蛋的
http://blog.csdn.net/gqqnb/article/details/42142639
http://bookshadow.com/weblog/2014/12/14/leetcode-maximum-gap/
'''

class Solution(object):
    # :type nums: List[int]
    # :rtype: int
    def maximumGap(self, nums): # nums中的数都是非负的 并且在32bit范围内
        if len(nums) < 2:
            return 0
        min_n, max_n = min(nums), max(nums)
        bk_len = max(1, int(math.ceil(float(max_n - min_n) / (N - 1))))   # ceil表示向上取整 bk_len表示每个区间长度
        bk_num = (max_n - min_n) / bk_len + 1 # bk_num表示区间个数 不直接用len(nums)是因为有可能nums中有许多重复元素
        bks = [[] for i in range(bk_num)]    # 区间范围 左闭右开 [min, min+bk_len) [min+2*bk_len, min+3*bk_len) .. [max, nouse)
        for n in nums:
            loc = (n - min_n) / bk_len  # loc定位n到哪个区间
            bks[loc].append(n)
        max_gap, last_max = 0, 0
        for i in range(len(bks)):
            if bks[i]:  # 有可能有些bk没有任何元素
                max_gap = max(max_gap, min(bks[i]) - last_max) if i != 0 else 0
                last_max = max(bks[i])
        return max_gap

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumGap([1, 1, 1, 1]))
    print(sol.maximumGap([3, 2, 3]))