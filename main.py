import pygame
import sys

pygame.init()

window_width = 1000
window_height = 750

screen = pygame.display.set_mode((window_width, window_height))
background_colour = (255, 255, 255)

pygame.display.set_caption("Pygame test")

screen.fill(background_colour)


class Button:
    def __init__(self, pos_x, pos_y, width, height, text, colour=(179, 179, 204)):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))

        font = pygame.font.SysFont(None, 32)
        button_text = font.render(self.text, True, (0, 0, 0))

        screen.blit(button_text, (self.pos_x + (self.width/2 - button_text.get_width()/2),
                    self.pos_y + (self.height/2 - button_text.get_height()/2)))

    def is_over(self, mouse_x, mouse_y):
        if self.pos_x < mouse_x < (self.pos_x + self.width):
            if self.pos_y < mouse_y < (self.pos_y + self.height):
                return True

        return False


def print_board_console(board):
    for i in range(0, 9):
        print("| ", end="")
        for j in range(0, 9):
            print(str(board[i][j]) + " | ", end="")
        print()


def print_board_gui(board, board_x, board_y):
    for i in range(0, 9):
        for j in range(0, 9):
            add_number_to_gui(board, i, j, board_x, board_y)


def draw_blank_board(pos_x, pos_y, square_width):

    background = pygame.Rect(pos_x, pos_y, (square_width + 1) * 9 + 1, (square_width + 1) * 9 + 1)
    pygame.draw.rect(screen, (0, 0, 0), background)

    x = pos_x + 1
    y = pos_y + 1

    for i in range(9):
        for j in range(9):
            square = pygame.Rect(x, y, square_width, square_width)
            pygame.draw.rect(screen, (255, 255, 255), square)

            x += square_width + 1

        x = pos_x + 1
        y += square_width + 1


def add_number_to_gui(board, pos_x, pos_y, board_x, board_y):
    num_x = board_x + 51 * pos_x + 17
    num_y = board_y + 51 * pos_y + 10

    square = pygame.Rect(num_x, num_y, 30, 35)
    pygame.draw.rect(screen, (255, 255, 255), square)

    board_num = board[pos_y][pos_x]

    if board_num != 0:
        font = pygame.font.SysFont(None, 48)
        text = font.render(str(board_num), True, (0, 0, 0))
        screen.blit(text, (num_x, num_y))


def clear_board(board, board_x, board_y):
    for i in range(0, 9):
        for j in range(0, 9):

            board[i][j] = 0

            num_x = board_x + 51 * i + 17
            num_y = board_y + 51 * j + 10

            square = pygame.Rect(num_x, num_y, 30, 35)
            pygame.draw.rect(screen, (255, 255, 255), square)


def custom_solve():

    screen.fill(background_colour)

    font = pygame.font.SysFont(None, 48)

    solve_button = Button(250, 25, 200, 50, "Solve Puzzle")
    solve_button.draw()

    clear_button = Button(550, 25, 200, 50, "Clear Puzzle")
    clear_button.draw()

    draw_blank_board(270, 100, 50)

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_board_gui(board, 270, 100)

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

            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if solve_button.is_over(mouse_x, mouse_y) and (solve_button.colour != (209, 209, 224)):
                    solve_button.colour = (209, 209, 224)
                    solve_button.draw()
                elif (not solve_button.is_over(mouse_x, mouse_y)) and solve_button.colour != (179, 179, 204):
                    solve_button.colour = (179, 179, 204)
                    solve_button.draw()

                if clear_button.is_over(mouse_x, mouse_y) and (clear_button.colour != (209, 209, 224)):
                    clear_button.colour = (209, 209, 224)
                    clear_button.draw()
                elif (not clear_button.is_over(mouse_x, mouse_y)) and clear_button.colour != (179, 179, 204):
                    clear_button.colour = (179, 179, 204)
                    clear_button.draw()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if clear_button.is_over(mouse_x, mouse_y):
                    clear_board(board, 270, 100)

                if solve_button.is_over(mouse_x, mouse_y):

                    while not check_board_complete(board):
                        if check_square(board, 0, 0):
                            print_board_gui(board, 270, 100)
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


def main_menu():

    screen.fill(background_colour)

    font = pygame.font.SysFont(None, 72)

    text = font.render("Sudoku Solver", True, (0, 0, 0))

    screen.blit(text, ((window_width/2 - text.get_width()/2), 100))

    example_button = Button(300, 200, 400, 50, "Solve Example Puzzle")
    example_button.draw()

    custom_button = Button(300, 300, 400, 50, "Solve Custom Puzzle")
    custom_button.draw()

    instruction_button = Button(300, 400, 400, 50, "Read Instructions")
    instruction_button.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if example_button.is_over(mouse_x, mouse_y) and (example_button.colour != (209, 209, 224)):
                    example_button.colour = (209, 209, 224)
                    example_button.draw()
                elif (not example_button.is_over(mouse_x, mouse_y)) and example_button.colour != (179, 179, 204):
                    example_button.colour = (179, 179, 204)
                    example_button.draw()

                if custom_button.is_over(mouse_x, mouse_y) and (custom_button.colour != (209, 209, 224)):
                    custom_button.colour = (209, 209, 224)
                    custom_button.draw()
                elif (not custom_button.is_over(mouse_x, mouse_y)) and custom_button.colour != (179, 179, 204):
                    custom_button.colour = (179, 179, 204)
                    custom_button.draw()

                if instruction_button.is_over(mouse_x, mouse_y) and (instruction_button.colour != (209, 209, 224)):
                    instruction_button.colour = (209, 209, 224)
                    instruction_button.draw()
                elif (not instruction_button.is_over(mouse_x, mouse_y)) and instruction_button.colour != (179, 179, 204):
                    instruction_button.colour = (179, 179, 204)
                    instruction_button.draw()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if example_button.is_over(mouse_x, mouse_y):
                    example_puzzle()

                if instruction_button.is_over(mouse_x, mouse_y):
                    pass

                if custom_button.is_over(mouse_x, mouse_y):
                    custom_solve()

        pygame.display.update()


def example_puzzle():

    screen.fill(background_colour)

    solve_button = Button(250, 25, 200, 50, "Solve Puzzle")
    solve_button.draw()

    clear_button = Button(550, 25, 200, 50, "Clear Puzzle")
    clear_button.draw()

    easy_button = Button(150, 100, 200, 50, "Easy Puzzle")
    easy_button.draw()

    medium_button = Button(400, 100, 200, 50, "Medium Puzzle")
    medium_button.draw()

    hard_button = Button(650, 100, 200, 50, "Hard Puzzle")
    hard_button.draw()

    draw_blank_board(270, 200, 50)

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_board_gui(board, 270, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if solve_button.is_over(mouse_x, mouse_y) and (solve_button.colour != (209, 209, 224)):
                    solve_button.colour = (209, 209, 224)
                    solve_button.draw()
                elif (not solve_button.is_over(mouse_x, mouse_y)) and solve_button.colour != (179, 179, 204):
                    solve_button.colour = (179, 179, 204)
                    solve_button.draw()

                if easy_button.is_over(mouse_x, mouse_y) and (easy_button.colour != (209, 209, 224)):
                    easy_button.colour = (209, 209, 224)
                    easy_button.draw()
                elif (not easy_button.is_over(mouse_x, mouse_y)) and easy_button.colour != (179, 179, 204):
                    easy_button.colour = (179, 179, 204)
                    easy_button.draw()

                if medium_button.is_over(mouse_x, mouse_y) and (medium_button.colour != (209, 209, 224)):
                    medium_button.colour = (209, 209, 224)
                    medium_button.draw()
                elif (not medium_button.is_over(mouse_x, mouse_y)) and medium_button.colour != (179, 179, 204):
                    medium_button.colour = (179, 179, 204)
                    medium_button.draw()

                if hard_button.is_over(mouse_x, mouse_y) and (hard_button.colour != (209, 209, 224)):
                    hard_button.colour = (209, 209, 224)
                    hard_button.draw()
                elif (not hard_button.is_over(mouse_x, mouse_y)) and hard_button.colour != (179, 179, 204):
                    hard_button.colour = (179, 179, 204)
                    hard_button.draw()

                if clear_button.is_over(mouse_x, mouse_y) and (clear_button.colour != (209, 209, 224)):
                    clear_button.colour = (209, 209, 224)
                    clear_button.draw()
                elif (not clear_button.is_over(mouse_x, mouse_y)) and clear_button.colour != (179, 179, 204):
                    clear_button.colour = (179, 179, 204)
                    clear_button.draw()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if clear_button.is_over(mouse_x, mouse_y):
                    clear_board(board, 270, 200)

                if solve_button.is_over(mouse_x, mouse_y):

                    while not check_board_complete(board):
                        if check_square(board, 0, 0):
                            print_board_gui(board, 270, 200)
                            print("Done")

                if easy_button.is_over(mouse_x, mouse_y):
                    board = sample_puzzle("easy")
                    print_board_gui(board, 270, 200)

                if medium_button.is_over(mouse_x, mouse_y):
                    board = sample_puzzle("medium")
                    print_board_gui(board, 270, 200)

                if hard_button.is_over(mouse_x, mouse_y):
                    board = sample_puzzle("hard")
                    print_board_gui(board, 270, 200)

        pygame.display.update()


def sample_puzzle(difficulty):
    if difficulty == "easy":
        return [
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

    elif difficulty == "medium":
        return [
            [0, 0, 1, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 8, 4, 0, 0, 5, 0],
            [0, 8, 0, 0, 0, 0, 0, 1, 0],
            [0, 6, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 7, 6, 0, 0, 3, 0, 0],
            [0, 1, 0, 9, 0, 0, 0, 0, 7],
            [0, 2, 5, 0, 0, 0, 0, 8, 0],
            [7, 0, 0, 0, 0, 4, 2, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0]
        ]

    elif difficulty == "hard":

        return [
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
    main_menu()
