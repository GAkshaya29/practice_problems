class Solution:
    def solveSudoku(self, board):
        # code here
        def canWePlace(row,col,num,board):                 
            # row and col check 
            for i in range(0,9):  
                if(board[row][i] == num or board[i][col] == num):
                    return False 
            start_row , start_col = 3*(row//3),3*(col//3)
            for i in range(start_row,start_row+3):
                for j in range(start_col,start_col+3):
                    if(board[i][j] == num):
                        return False 
            return True 
        def solve(board):
            n = 9               
            for row in range(0,n):
                for col in range(0,n):
                    if(board[row][col] == 0):
                        for num in range(1,10):
                            if(canWePlace(row,col,num,board)):
                                board[row][col] = num
                                if(solve(board)): 
                                    return True 
                                board[row][col] = 0 
                        return False
            return True
        solve(board)
