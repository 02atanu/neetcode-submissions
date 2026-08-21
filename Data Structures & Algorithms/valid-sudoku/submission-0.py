class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # To check rows
        def check_rows() -> bool:
            
            for row in board:
                seen = set()
                for digit in row:
                    if digit == ".":
                        continue
                    else:
                        if digit in seen:
                            return False
                        seen.add(digit)
            return True

        # Check columns
        def check_columns() -> bool:
            for i in range(9):
                seen = set()
                for j in range(9): # Since it's 9x9 board

                    cell = board[j][i]
                    if cell == ".":
                        continue
                    else:
                        if cell in seen:
                            return False
                        seen.add(cell)
            return True

        # Check 3X3 grids
        def check_grids():
            def check_3x3(center: tuple) -> bool:
                seen = set()

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # Get the current cell
                        cell = board[center[0] + i][center[1] + j]

                        if cell == ".":
                            continue
                        else:
                            if cell in seen:
                                return False
                            seen.add(cell)
                return True
            # Define centers and run check grid:
            centers = [(i, j) for i in range(1,10,3) for j in range(1, 10, 3)]
            for center in centers:
                if not check_3x3(center):
                    return False
            return True

        return check_rows() and check_columns() and check_grids()