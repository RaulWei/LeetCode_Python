# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
ugly_num 素数分解仅仅由2 3 5的乘方的乘积构成
'''

class Solution(object):
    def isUgly(self, num):
        """
          :type num: int
          :rtype: bool
          """
        if num == 0:
            return False
        if num == 1:
            return True
        ugly_prime_factors = [2, 3, 5]
        for i in range(len(ugly_prime_factors)):
            while num % ugly_prime_factors[i] == 0:
                num /= ugly_prime_factors[i]
        if num == 1:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isUgly(3))
    print(sol.isUgly(4))
    print(sol.isUgly(14))