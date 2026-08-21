class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            row_set = set()
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in row_set:
                    return False
                row_set.add(val)

        for col in range(9):
            col_set = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in col_set:
                    return False
                col_set.add(val)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        val = board[row][col]

                        if val == ".":
                            continue

                        if val in box_set:
                            return False
                        box_set.add(val)
        return True
                
                    



        #[[1,2,,],
        #[4,,,],
        #[,9,8]]