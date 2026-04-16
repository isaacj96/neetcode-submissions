class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check_row = [x for x in board[i] if x != '.']
            if len(check_row) != len(set(check_row)):
                return False
            check_col = [board[r][i] for r in range(9) if board[r][i] != '.']
            if len(check_col) != len(set(check_col)):
                return False
            
            start_row = (i // 3) * 3
            start_col = (i % 3) * 3
            check_box = []

            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] != '.':
                        check_box.append(board[r][c])
            if len(check_box) != len(set(check_box)):
                return False
                
        return True