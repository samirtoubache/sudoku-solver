def print_board(board):
    for i in range(0, 9):
        print("| ", end="")
        for j in range(0, 9):
            print(str(board[i][j]) + " | ", end="")
        print()


def main():
    board = [
        [0, 3, 7, 8, 0, 0, 2, 9, 1],
        [0, 0, 1, 7, 0, 6, 0, 3, 0],
        [5, 9, 4, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 8, 7, 5],
        [2, 0, 0, 0, 6, 7, 0, 1, 0],
        [0, 0, 0, 0, 4, 8, 9, 0, 0],
        [3, 6, 5, 2, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 1, 3, 6, 0, 2],
        [0, 1, 0, 6, 0, 0, 3, 0, 9]
    ]

    while not check_board_complete(board):
        if check_square(board, 0, 0):
            print_board(board)
            print()


def check_board_complete(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return False

    return True


def check_square(board, x_pos, y_pos):

    if y_pos >= 9:
        y_pos = 0
        x_pos += 1

    current_square = (x_pos * 9) + y_pos

    # cycled through every square
    if current_square == 81:
        return True

    # default number in the puzzle
    elif board[x_pos][y_pos] != 0:
        return check_square(board, x_pos, y_pos + 1)

    # blank space
    else:
        for i in range(1, 10):

            # if i is a valid value for this location
            if check_square_value(board, x_pos, y_pos, i):
                board[x_pos][y_pos] = i
                status = check_square(board, x_pos, y_pos + 1)

                if not status:
                    continue
                else:
                    return True

    # If this point is reached, they are no correct values for this position, meaning a previous value is incorrect
    # set this square to the blank value and return False indicating a previous square must be changed
    board[x_pos][y_pos] = 0
    return False


def check_square_value(board, x_pos, y_pos, value):

    # check row
    for y in range(0, 9):
        if board[x_pos][y] == value:
            return False

    # check column
    for x in range(0, 9):
        if board[x][y_pos] == value:
            return False

    x_start = (x_pos // 3) * 3
    y_start = (y_pos // 3) * 3

    # check 3 x 3 square
    for i in range(x_start, x_start + 3):
        for j in range(y_start, y_start + 3):
            if board[i][j] == value:
                return False

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
