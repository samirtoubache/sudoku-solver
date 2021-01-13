import pygame
import sys


def print_board_console(board):
    for i in range(0, 9):
        print("| ", end="")
        for j in range(0, 9):
            print(str(board[i][j]) + " | ", end="")
        print()


def print_board_gui(screen, board):
    for i in range(0, 9):
        for j in range(0, 9):
            add_number_to_gui(screen, board, i, j)


def draw_board(screen):

    x = 271
    y = 101

    solve_button = pygame.Rect(400, 25, 200, 50)
    pygame.draw.rect(screen, (0, 0, 0), solve_button)

    font = pygame.font.SysFont(None, 32)

    text = font.render("Solve Puzzle", True, (255, 255, 255))

    screen.blit(text, (435, 40))

    background = pygame.Rect(270, 100, 51 * 9 + 1, 51 * 9 + 1)
    pygame.draw.rect(screen, (0, 0, 0), background)

    for i in range(9):
        for j in range(9):

            square = pygame.Rect(x, y, 50, 50)

            pygame.draw.rect(screen, (255, 255, 255), square)

            x += 51

        x = 271
        y += 51


def add_number_to_gui(screen, board, pos_x, pos_y):
    num_x = 270 + 51 * pos_x + 17
    num_y = 100 + 51 * pos_y + 10

    square = pygame.Rect(num_x, num_y, 30, 35)
    pygame.draw.rect(screen, (255, 255, 255), square)

    board_num = board[pos_y][pos_x]

    if board_num != 0:
        font = pygame.font.SysFont(None, 48)
        text = font.render(str(board_num), True, (0, 0, 0))
        screen.blit(text, (num_x, num_y))


def main():

    pygame.init()

    window_width = 1000
    window_height = 600

    screen = pygame.display.set_mode((window_width, window_height))

    background_colour = (255, 255, 255)

    pygame.display.set_caption("Pygame test")

    screen.fill(background_colour)

    font = pygame.font.SysFont(None, 48)

    draw_board(screen)

    # board = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]

    board = [
        [0, 0, 0, 7, 0, 0, 0, 0, 4],
        [6, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 4, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [7, 0, 6, 0, 5, 0, 9, 0, 0],
        [0, 0, 3, 0, 0, 8, 2, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 4, 0, 9, 3],
        [0, 1, 0, 0, 7, 0, 5, 0, 0]
    ]

    print_board_gui(screen, board)

    num = -1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    while not check_board_complete(board):
                        if check_square(board, 0, 0):
                            print_board_console(board)
                            print()

                if event.key == pygame.K_0:
                    num = 0
                elif event.key == pygame.K_1:
                    num = 1
                elif event.key == pygame.K_2:
                    num = 2
                elif event.key == pygame.K_3:
                    num = 3
                elif event.key == pygame.K_4:
                    num = 4
                elif event.key == pygame.K_5:
                    num = 5
                elif event.key == pygame.K_6:
                    num = 6
                elif event.key == pygame.K_7:
                    num = 7
                elif event.key == pygame.K_8:
                    num = 8
                elif event.key == pygame.K_9:
                    num = 9

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if 400 < mouse_x < 600 and 25 < mouse_y < 75:

                    while not check_board_complete(board):
                        if check_square(board, 0, 0):
                            print_board_gui(screen, board)
                            print("Done")

                elif 270 < mouse_x < 730 and 100 < mouse_y < 560:
                    pos_x = (mouse_x - 270) // 51
                    pos_y = (mouse_y - 100) // 51

                    print("Square: " + str(pos_x) + ", " + str(pos_y))

                    if num != -1:

                        num_x = 270 + 51 * pos_x + 17
                        num_y = 100 + 51 * pos_y + 10

                        if num == 0:
                            square = pygame.Rect(num_x, num_y, 30, 35)
                            pygame.draw.rect(screen, (255, 255, 255), square)

                        else:
                            # If there is another number on the board, hide it first
                            if board[pos_y][pos_x] != 0:
                                square = pygame.Rect(num_x, num_y, 30, 35)
                                pygame.draw.rect(screen, (255, 255, 255), square)

                            text = font.render(str(num), True, (0, 0, 0))

                            screen.blit(text, (num_x, num_y))

                        board[pos_y][pos_x] = num

                        print_board_console(board)

        pygame.display.update()

        # board1 = [
        #     [0, 3, 7, 8, 0, 0, 2, 9, 1],
        #     [0, 0, 1, 7, 0, 6, 0, 3, 0],
        #     [5, 9, 4, 0, 2, 0, 0, 0, 0],
        #     [0, 0, 0, 9, 0, 0, 8, 7, 5],
        #     [2, 0, 0, 0, 6, 7, 0, 1, 0],
        #     [0, 0, 0, 0, 4, 8, 9, 0, 0],
        #     [3, 6, 5, 2, 0, 0, 0, 0, 0],
        #     [9, 0, 0, 0, 1, 3, 6, 0, 2],
        #     [0, 1, 0, 6, 0, 0, 3, 0, 9]
        # ]
        #
        # board = [
        #     [0, 0, 0, 7, 0, 0, 0, 0, 4],
        #     [6, 0, 0, 0, 0, 0, 8, 0, 0],
        #     [0, 4, 0, 5, 0, 1, 0, 0, 0],
        #     [0, 0, 0, 1, 0, 0, 0, 0, 0],
        #     [7, 0, 6, 0, 5, 0, 9, 0, 0],
        #     [0, 0, 3, 0, 0, 8, 2, 0, 0],
        #     [0, 0, 0, 2, 0, 0, 0, 0, 0],
        #     [0, 0, 8, 0, 0, 4, 0, 9, 3],
        #     [0, 1, 0, 0, 7, 0, 5, 0, 0]
        # ]
        #
        # while not check_board_complete(board1):
        #     if check_square(board1, 0, 0):
        #         print_board_console(board1)
        #         print()


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
