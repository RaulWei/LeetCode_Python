# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
两条竖线与x轴组成的区域 收集最多雨水
'''

class Solution:
    def getArea(self, height, left, right):
        if right >= left:
            return min(height[left], height[right]) * (right - left)
        return 0

    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if len(height) <= 1:
            return 0
        mleft, mright = 0, len(height) - 1
        left, right = mleft, mright
        mArea = self.getArea(height, left, right)
        # if height[left] < height[right]:
        while left < len(height):
            while left < len(height) - 1 and height[left] >= height[left+1]:
                left += 1
            left += 1
            right = mright
            while right >= 0:
                if mArea < self.getArea(height, left, right):
                    mArea = self.getArea(height, left, right)
                    mleft = left
                    mright = right
                while right > 0 and height[right] >= height[right - 1]:
                    right -= 1
                right -= 1
                if left >= right:
                    break

        return mArea
            # while left < right:
            #     while left < len(height) - 1 and height[left] >= height[left+1]:
            #         left += 1
            #     left += 1
            #     if mArea < self.getArea(height, left, right):
            #         mArea = self.getArea(height, left, right)
            #     while right > 0 and height[right] >= height[right - 1]:
            #         right -= 1
            #     right -= 1
            #     if mArea < self.getArea(height, left, right):
            #         mArea = self.getArea(height, left, right)
            # return mArea

if __name__ == '__main__':
    sol = Solution()
    # print(sol.maxArea([1, 2, 4, 3]))
    print(sol.maxArea([2, 3, 10, 5, 7, 8, 9]))