def squareinator(board):
    """
    turns a sudoku board made of rows into its corresponding squares
    :param board:
    :type board: List[List[str]]
    :return list of squares in board:
    :rtype: List[List[str]]
    """
    list_num = 0
    start_pos = 0
    square_len = 3
    squares = []
    # loops through the board to finds the 3x3 squares
    for i in range(len(board)):
        # curr_square is slicing the 3 needed lists
        curr_square = board[list_num][start_pos:square_len] \
                      + board[list_num + 1][start_pos:square_len] + board[list_num + 2][start_pos:square_len]
        squares.append(curr_square)  # store the square
        # after first iteration, we need to find the next two squares, shifting by 3 because square is len(3)
        start_pos += 3
        square_len += 3
        # shifts the row count to the next set of squares
        if (i == 2) or (i == 5):
            list_num += 3
            start_pos = 0
            square_len = 3
    return squares

def columinator(board):
    """
    Turns the board column-wise.
    :param board: List of lists representing the board.
    :type board: List[List[str]]
    :return: List of squares in board, organized column-wise.
    :rtype: List[List[str]]
    """
    # Determine the number of rows and columns in the board
    num_rows = len(board)
    num_cols = len(board[0])

    # Initialize the result list with empty lists for each column
    col_wise = [[] for _ in range(num_cols)]

    # Iterate over the rows and columns, adding elements to the appropriate column
    for row_cell in range(num_rows):
        for col_cell in range(num_cols):
            col_wise[col_cell].append(board[row_cell][col_cell])

    return col_wise

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    squares = squareinator(board)
    columns = columinator(board)
    is_valid = False
    edge_case_met = False

    # empty board catcher
    sum = 0
    for row in board:
        sum += row.count(".")
        if sum == 81:
            is_valid = True
            return is_valid

    # column wise checker
    for row in board:
        for cell in row:
            # ignore empty cells
            if cell != ".":
                # count total copies of number
                double_check = row.count(cell)
                # checking for edge case where the number in a cell is too large
                if (int(cell) <= 0) or (int(cell) > 9):
                    is_valid = False
                    edge_case_met = True
                    break
                # if there are more than 1 of the same num in a row, edge case is met, and board not valid
                if double_check > 1:
                    is_valid = False
                    edge_case_met = True
                    break
                # if only 1 of the items or less are in a row then board valid
                elif double_check <= 1:
                    is_valid = True
        # breaks the whole loop upon meeting edge case
        if edge_case_met:
            break
    # skip if already found false to avoid unneccessary computing
    if not edge_case_met:
        # sqaure wise comparisons
        for square in squares:
            for cell in square:
                # again ignore the null values
                if cell != ".":
                    double_check = square.count(cell)
                    if double_check > 1:
                        is_valid = False
                        edge_case_met = True
                        break
                    elif double_check <= 0:
                        is_valid = True
            if edge_case_met:
                break
        # same as before but for the column comparisons
        for column in columns:
            for cell in column:
                if cell != ".":
                    double_check = column.count(cell)
                    if double_check > 1:
                        is_valid = False
                        edge_case_met = True
                        break
                    elif double_check <= 0:
                        is_valid = True
            if edge_case_met:
                break

    return is_valid


