# -*- coding: UTF-8 -*-
__author__ = 'wang'

'''
1 从边界找到'O'
2 使用BFS把找到的'O'标记为'T'
3 遍历board 把'O'转换为'X' 把'T'转换为'O'
'''

class Solution(object):
    # :type board: List[List[str]]
    # :rtype: void Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board:
            return
        row_n, col_n = len(board), len(board[0])
        # 边界：第一行 和 最后一行
        for j in range(col_n):
            if board[0][j] == 'O':
                self.bfsMark(board, 0, j, row_n, col_n)
            if board[row_n - 1][j] == 'O':
                self.bfsMark(board, row_n - 1, j, row_n, col_n)
        # 边界：最左列 和 最右列
        for i in range(row_n):
            if board[i][0] == 'O':
                self.bfsMark(board, i, 0, row_n, col_n)
            if board[i][col_n - 1] == 'O':
                self.bfsMark(board, i, col_n - 1, row_n, col_n)
        # 遍历board
        for i in range(row_n):
            for j in range(col_n):
                if board[i][j] == 'O':
                    board[i] = ''.join(board[i][:j]) + 'X' + ''.join(board[i][j + 1:])
                if board[i][j] == 'T':
                    board[i] = ''.join(board[i][:j]) + 'O' + ''.join(board[i][j + 1:])

    def bfsMark(self, board, row, col, row_n, col_n):
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上 下 左 右
        queue = [[row, col]]
        while queue:
            cur_row, cur_col = queue[0][0], queue[0][1]
            queue.pop(0)
            if board[row][col] == 'O':
                board[cur_row] = ''.join(board[cur_row][:cur_col]) + 'T' + ''.join(board[cur_row][cur_col + 1:])
            for dc in direction:
                update_row, update_col = cur_row + dc[0], cur_col + dc[1]
                if 0 <= update_row < row_n and 0 <= update_col < col_n and board[update_row][update_col] == 'O':
                    # 加入队列的时候要做标记 否则容易被重复加入队列造成死循环
                    board[update_row] = ''.join(board[update_row][:update_col]) + 'T' + ''.join(board[update_row][update_col + 1:])
                    queue.append([update_row, update_col])


if __name__ == '__main__':
    sol = Solution()
    sol.solve(["XOOOOOOOOOOOOOOOOOOO","OXOOOOXOOOOOOOOOOOXX","OOOOOOOOXOOOOOOOOOOX","OOXOOOOOOOOOOOOOOOXO","OOOOOXOOOOXOOOOOXOOX","XOOOXOOOOOXOXOXOXOXO","OOOOXOOXOOOOOXOOXOOO","XOOOXXXOXOOOOXXOXOOO","OOOOOXXXXOOOOXOOXOOO","XOOOOXOOOOOOXXOOXOOX","OOOOOOOOOOXOOXOOOXOX","OOOOXOXOOXXOOOOOXOOO","XXOOOOOXOOOOOOOOOOOO","OXOXOOOXOXOOOXOXOXOO","OOXOOOOOOOXOOOOOXOXO","XXOOOOOOOOXOXXOOOXOO","OOXOOOOOOOXOOXOXOXOO","OOOXOOOOOXXXOOXOOOXO","OOOOOOOOOOOOOOOOOOOO","XOOOOXOOOXXOOXOXOXOO"])
    sol.solve(["XOX", "OXO", "XOX"])
    sol.solve(["O"])
    sol.solve(["OOO", "OOO", "OOO"])
    sol.solve(["X"])
    sol.solve(["XXXX", "XOOX", "XXOX", "XOXX"])