def print_board(board):
    for i in range(0, 9):
        print("| ", end="")
        for j in range(0, 9):
            square = (i * 9) + j
            print(str(board[square]) + " | ", end="")
        print()


def main():
    board = [
        0, 3, 7, 8, 0, 0, 2, 9, 1,
        0, 0, 1, 7, 0, 6, 0, 3, 0,
        5, 9, 4, 0, 2, 0, 0, 0, 0,
        0, 0, 0, 9, 0, 0, 8, 7, 5,
        2, 0, 0, 0, 6, 7, 0, 1, 0,
        0, 0, 0, 0, 4, 8, 9, 0, 0,
        3, 6, 5, 2, 0, 0, 0, 0, 0,
        9, 0, 0, 0, 1, 3, 6, 0, 2,
        0, 1, 0, 6, 0, 0, 3, 0, 9
    ]

    while not check_board_complete(board):
        board = check_square(board, 0, 0)

    print_board(board)
    print()


def check_board_complete(board):
    for i in range(0, 9):
        for j in range(0, 9):
            square = (i * 9) + j
            if board[square] == 0:
                return False

    return True


def check_square(board, x_pos, y_pos):

    if y_pos >= 9:
        y_pos = 0
        x_pos += 1

    current_square = (x_pos * 9) + y_pos

    # cycled through every square
    if current_square == 81:
        return board
    elif board[current_square] != 0:
        return check_square(board, x_pos, y_pos + 1)
    else:
        options = {
            1: True,
            2: True,
            3: True,
            4: True,
            5: True,
            6: True,
            7: True,
            8: True,
            9: True
        }

        # check row
        for i in range(x_pos * 9, (x_pos * 9) + 9):
            if board[i] != 0:
                options[board[i]] = False

        # check column
        for j in range(y_pos, y_pos + 81, 9):
            if board[j] != 0:
                options[board[j]] = False

        x_start = (x_pos // 3) * 3
        y_start = (y_pos // 3) * 3

        # check 3 x 3 square
        for i in range(x_start, x_start + 3):
            for j in range(y_start, y_start + 3):
                square = (i * 9) + j
                if board[square] != 0:
                    options[board[square]] = False

        choices = 0

        for key in options:
            if options[key]:
                choices += 1
                # board[current_square] = key

        # while not check_board_complete(board):
        #     return check_square(board, x_pos, y_pos + 1)

        if choices == 1:
            for key in options:
                if options[key]:
                    board[current_square] = key

        return check_square(board, x_pos, y_pos + 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
