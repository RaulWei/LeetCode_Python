# -*- coding: UTF-8 -*-
__author__ = 'weimw'

'''
只验证摆法是否合法 不验证是否有解
数独规则：每行每列每个小九宫格都包含1~9
'''

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        length = len(board)
        # row
        for i in range(length):
            valid = [0] * 10
            for j in range(length):
                if not self.isValidNum(valid, board[i][j]):
                    return False
        # col
        for j in range(length):
            valid = [0] * 10
            for i in range(length):
                if not self.isValidNum(valid, board[i][j]):
                    return False
        # subbox
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                valid = [0] * 10
                for k in range(9):
                    if not self.isValidNum(valid, board[i + k / 3][j + k % 3]):
                        return False
                j += 3
            i += 3
        return True

    def isValidNum(self, valid, num):
        if num == '.':
            return True
        if 1 <= int(num) <= 9 and valid[int(num)] == 0:
            valid[int(num)] = 1
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSudoku(["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]))
    print(sol.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]))
    print(sol.isValidSudoku(["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."]))