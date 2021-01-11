import pygame
import sys


def print_board(board):
    for i in range(0, 9):
        print("| ", end="")
        for j in range(0, 9):
            print(str(board[i][j]) + " | ", end="")
        print()


def draw_board(screen):

    x = 271
    y = 101

    background = pygame.Rect(270, 100, 51 * 9 + 1, 51 * 9 + 1)
    pygame.draw.rect(screen, (0, 0, 0), background)

    for i in range(9):
        for j in range(9):

            square = pygame.Rect(x, y, 50, 50)

            pygame.draw.rect(screen, (255, 255, 255), square)

            x += 51

        x = 271
        y += 51


def main():

    pygame.init()

    window_width = 1000
    window_height = 600

    screen = pygame.display.set_mode((window_width, window_height))

    background_colour = (255, 255, 255)

    pygame.display.set_caption("Pygame test")

    screen.fill(background_colour)

    draw_board(screen)

    font = pygame.font.SysFont(None, 48)

    num = -1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
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

                print(num)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if 270 < mouse_x < 730 and 100 < mouse_y < 560:
                    pos_x = (mouse_x - 270) // 51
                    pos_y = (mouse_y - 100) // 51

                    print("Square: " + str(pos_x) + ", " + str(pos_y))


                    # while number:
                    #     if event.type == pygame.MOUSEBUTTONDOWN:
                    #         print("yoyo")
                    #         mouse_x_2 = event.pos[0]
                    #         mouse_y_2 = event.pos[1]
                    #
                    #         if 0 < mouse_x_2 < 100 and 0 < mouse_y_2 < 100:
                    #             number = False

                    text = font.render(str(num), True, (0, 0, 0,))

                    num_x = 270 + 51 * pos_x + 17
                    num_y = 100 + 51 * pos_y + 10

                    screen.blit(text, (num_x, num_y))

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
        # while not check_board_complete(board):
        #     if check_square(board, 0, 0):
        #         print_board(board)
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
